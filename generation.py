import os
import subprocess
import argparse
from markdownmaker.document import Document
from markdownmaker.markdownmaker import *
from sqlalchemy import create_engine, Column, Integer, String, Sequence, inspect
from mdutils.mdutils import MdUtils
import re
import textwrap
import openai
from openai import OpenAI


def read_dbml_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            dbml_content = file.read()
        return dbml_content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def generate_description(text, key):
    client = OpenAI(api_key=key)

    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": """You will be provided with the code representing database table. Generate description of this table, 
        description should try to guess the semantics using table and column names, and should take any additional information, 
        such as comments, constraints and relationships into account."""
        },
        {
        "role": "user",
        "content": f"""{text}"""
        }
    ],
    temperature=0.7,
    max_tokens=512,
    top_p=1
    )

    return response.choices[0].message.content

def generate_general_description(text, key):
    client = OpenAI(api_key=key)

    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": """You will be provided with the code representing database. Generate description of databse in 4 sentences, 
                    general overviwe, what it is representing. (only text, not subpoints)"""
        },
        {
        "role": "user",
        "content": f"""{text}"""
        }
    ],
    temperature=0.7,
    max_tokens=512,
    top_p=1
    )

    return response.choices[0].message.content

def generate_report(user, password, host, port, database, openai_key):


    '''Connecting to postgres'''
    db_url = fr'postgresql://{user}:{password}@{host}:{port}/{database}'

    engine = create_engine(db_url)
    conn = engine.connect()
    insp = inspect(engine)

    '''Getting SQL syntax from databse'''
    command_1 = f'pg_dump --dbname=postgresql://{user}:{password}@{host}:{port}/{database} -s  > dump.sql'

    try:
        result = subprocess.run(command_1, shell=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)


    '''Getting DBML model from SQL'''
    command_2 = 'sql2dbml dump.sql --postgres'

    try:
        with open('dump.dbml', 'w') as file:
            result = subprocess.run(command_2, shell=True, stdout=file)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    
    '''Databse info'''

    '''Getting databse name'''
    database_name = engine.url.database
    '''Getting all tables'''
    all_tables = insp.get_table_names()
    '''Getting all schemas in database'''
    db_schemas = insp.get_schema_names()[1::]

    '''Generating databse description'''

    command_3 = f"sqlacodegen --noclasses --outfile model_test.txt {db_url}"
    try:
        result = subprocess.run(command_3, shell=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)

    '''Getting info from model about tables'''
    found_blocks = []
    with open('model_test.txt', 'r') as file:
        file_content = file.read()
        found_blocks.append(re.findall(r"(t_[\w]+ = Table\([\s\S]+?\)\n)",file_content))

    '''Getting indexes from .SQL'''
    indexes = []
    with open('dump.sql', 'r') as file:
        file_content = file.read()
        pattern = r'CREATE INDEX .*;'
        # pattern = r'CREATE INDEX "[\w]+" ON "\w+" \("\w+"\);'
        indexes.append(re.findall(pattern, file_content))
        # found_blocks.append(re.findall(pattern = r"CREATE INDEX '[\w]+' ON '\w+' \('\w+'\);", file_content))

        
    '''Getting DBML'''
    file_path = 'dump.dbml'
    dbml_text = read_dbml_from_file(file_path)


    '''Generating markdawn'''
    doc = Document()
    doc.add(Header(f"Database name: {database_name}"))
    with HeaderSubLevel(doc):
        doc.add(Header("General description"))

        doc.add(Paragraph(generate_general_description(file_content, openai_key)))

        doc.add(Header("Schemas"))

        doc.add(OrderedList(db_schemas))

        # Adding indexes
        doc.add(Header("Indexes"))
        if len(indexes[0]) == 0:
            doc.add(Paragraph("No indexes"))
        else:
            for i, el in enumerate(indexes[0]):
                    text = re.sub("CREATE", "", el)
                    doc.add(CodeBlock(text))

        # Adding tables and their descriptions
        doc.add(Header("Tables"))

        ordered_list = []

        for i, el in enumerate(all_tables):
            # Add each table as a list item
            ordered_list.append(Link(label=f'{el}<br>', url=f'#{el}'))

        doc.add(OrderedList(ordered_list))

        doc.add(Paragraph("***"))

        with HeaderSubLevel(doc):
            for i in all_tables:
                for block in found_blocks[0]:
                    # if f"'{i}'" in block:
                    if re.search(fr"\b{i}\b.*?metadata", block):
                        index = found_blocks[0].index(block)
                        # Find the index of the first matching elem
                        doc.add(Header(f"{i}"))
                        text = re.sub(r"t_\w+\s*=\s*Table\(", "", found_blocks[0][index])
                        pattern = r"'(\w+)',\s*metadata,"

                        # Using sub to replace the matched pattern with "table name = <table_name>\n"
                        text = re.sub(pattern, r"table name = '\1'\n", text)
                        lines = text.split('\n')
                        wrapped_lines = [textwrap.fill(line, width=80, replace_whitespace=False) for line in lines]
                        doc.add(CodeBlock('\n'.join(wrapped_lines)))
                        doc.add(Paragraph(Bold("Description")))
                        doc.add(Paragraph(generate_description(text, openai_key)))
                        doc.add(Paragraph("***"))


        doc.add(Header("Graph"))
        doc.add(f"""```{{.kroki dia='dbml' echo='false}}\n{dbml_text}\n```""")

    with open(f"{database_name}-description.md", "w") as f:
        f.write(doc.write())
    
    command_4 = f'pandoc {database_name}-description.md -o ../output/output.pdf -s --lua-filter filter-kroki.lua'
    
    try:
        subprocess.run(command_4, shell=True)

    except subprocess.CalledProcessError as e:
        print("Error:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Markdown content for a database and convert it to PDF.")
    parser.add_argument("user", help="Database user")
    parser.add_argument("password", help="Database password")
    parser.add_argument("host", help="Database host")
    parser.add_argument("port", help="Database port")
    parser.add_argument("database", help="Database name")
    parser.add_argument("openai_key", help="Openai key")


    args = parser.parse_args()
    generate_report(args.user, args.password, args.host, args.port, args.database, args.openai_key)