from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table, inspect, session
import sqlalchemy as sa

CONN_STR = '…'
engine = create_engine('sqlite:////home/friend/01-github/dw2ed/bd/python/load_existing_db/companies_1000.db')
metadata = MetaData()
insp = inspect(engine)
print(insp.get_table_names())

companias = Table('compania', metadata, 
  sa.Column("n", sa.String(50), primary_key=True),
  sa.Column("nome", sa.String(50)),
  sa.Column("dominio", sa.String(50)),
  sa.Column("ano", sa.String(50)),
  sa.Column("industria", sa.String(50)),
  sa.Column("tamanho", sa.String(50)),
  sa.Column("localizacao", sa.String(50)),
  sa.Column("pais", sa.String(50)),
  sa.Column("linkedin", sa.String(250)),
  sa.Column("empregados_atual", sa.Integer),
  sa.Column("empregados_total", sa.Integer)
)

with engine.connect() as conn:

    query = 'select * from compania'
    for row in conn.execute(query):
        print(row)

Session = sa.sessionmaker(bind=engine)
session = Session()

