from eralchemy2 import render_er
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
render_er(Base, 'erd_from_sqlalchemy.png')

## Draw from database
render_er("postgresql://postgres:jmrozek@localhost:5432/Project1", 'erd_from_sqlite.png')