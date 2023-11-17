from sqlalchemy import create_engine, MetaData
import sqlalchemy as sa
import sqlalchemy as db
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Sequence, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

# user = 'jmrozek'
# password = 'furm3w3sj5s7'
# host = 'lab.kis.agh.edu.pl'
# port = '1500'  # 5432 Domyślny port dla PostgreSQL
# database = 'jmrozek'

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

''' getting all tables'''
all_tables = insp.get_table_names()
print(all_tables)

'''getting table as df'''
df = pd.read_sql_table('actor', conn)
print(df)

'''getting all schemas in database'''
db_list = insp.get_schema_names()
print(db_list)

'''checking tables columns constraints'''

Base = declarative_base()

class User(Base):
    __tablename__ = 'actor'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    age = Column(Integer, index=True)

# Sprawdź zalożenia kolumny 'name'
print(f"Typ danych kolumny 'name': {User.__table__.c.name.type}")
print(f"Czy 'name' jest kluczem głównym? {User.__table__.c.name.primary_key}")
print(f"Czy 'name' może przyjmować wartości NULL? {User.__table__.c.name.nullable}")
print(f"Czy 'name' jest unikalny? {User.__table__.c.name.unique}")

