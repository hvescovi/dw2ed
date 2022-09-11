# ref:
# https://localcoder.org/sqlalchemy-existing-database-query

import sqlalchemy as sa

psw = "verysecret"
db = "accounts"

# create an engine
pengine = sa.create_engine('sqlite:///compania_1000.db')

from sqlalchemy.ext.declarative import declarative_base
# define declarative base
Base = declarative_base()

# reflect current database engine to metadata
metadata = sa.MetaData(pengine)
metadata.reflect()

# build your User class on existing `users` table
class Compania(Base):
    __table__ = sa.Table("compania", metadata)
    
# call the session maker factory
Session = sa.orm.sessionmaker(pengine)
session = Session()

# filter a record 
for c in session.query(Compania).all():
    print(c.id)
#session.query(Compania).filter(Compania.id==1).first()
