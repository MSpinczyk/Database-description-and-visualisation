from markdownmaker.document import Document
from markdownmaker.markdownmaker import *
import re
from sqlalchemy import create_engine, Column, Integer, String, Sequence, inspect
from mdutils.mdutils import MdUtils
import subprocess

'''CONNECTING TO POSTGRES'''
user = 'postgres'
password = 'jmrozek'
host = 'localhost'
port = '5432'  # 5432 Domyślny port dla PostgreSQL
database = 'Project1'

db_url = f'postgresql://{user}:{password}@{host}:{port}/{database}'
print(db_url)

engine = create_engine(db_url)
conn = engine.connect()
insp = inspect(engine)

''' DATABASE INFO'''

'''getting databse name'''
database_name = engine.url.database
''' getting all tables'''
all_tables = insp.get_table_names()
'''getting all schemas in database'''
db_schemas = insp.get_schema_names()[1::]


'''GENERATING DATABASE DESCRIPTION'''

# Command to run
command = f"sqlacodegen --outfile model.txt {db_url}"

try:
    # Run the command and capture the output
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)

except subprocess.CalledProcessError as e:
    # Handle any errors that occurred during the command execution
    print("Error:", e)



'''GETTING INFO FROM MODEL'''
pattern = re.compile(r'class\s.*?\n\n(?=\n)', re.DOTALL)
found_blocks = []

with open('C:\\Users\\Lenovo\\Desktop\\5year\\3-database-description-visualisation\\model.txt', 'r') as file:
    # Read the content of the file
    file_content = file.read()
    found_blocks.append(pattern.findall(file_content))
print(found_blocks)





''' GENERATING MARKDoWN'''
doc = Document()
doc.add(Header(f"Database name: {database_name}"))
with HeaderSubLevel(doc):
    doc.add(Header("Schemas"))
    doc.add(OrderedList(db_schemas))
    doc.add(Header("Tables"))
    for i, el in enumerate(all_tables):
        doc.add(Link(label=f'{i+1}. {el}<br>', url=f'#{el}'))

    with HeaderSubLevel(doc):
        for i in all_tables:
            for block in found_blocks[0]:
                if f"'{i}'" in block:
                    index = found_blocks[0].index(block)

            # Find the index of the first matching elem
            doc.add(Header(f"{i}"))
            doc.add(CodeBlock(found_blocks[0][index]))

with open(f"{database_name}-description.md", "w") as f:
    f.write(doc.write())
