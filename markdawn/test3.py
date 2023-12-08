from markdownmaker.document import Document
from markdownmaker.markdownmaker import *
from sqlalchemy import create_engine, Column, Integer, String, Sequence, inspect
from mdutils.mdutils import MdUtils


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

'''getting databse name'''
database_name = engine.url.database
''' getting all tables'''
all_tables = insp.get_table_names()
'''getting all schemas in database'''
db_schemas = insp.get_schema_names()[1::]

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
            doc.add(Header(f"{i}"))

with open(f"{database_name}-description.md", "w") as f:
    f.write(doc.write())
