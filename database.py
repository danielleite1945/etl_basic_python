from dotenv import load_dotenv
import sqlalchemy as sa
import os
from pandas import read_sql as pd_read_sql

load_dotenv()
DBUSER = os.getenv(f"DBUSER")
DBPWD = os.getenv(f"DBPWD")
DBHOST = os.getenv(f"DBHOST")
DBPORT = os.getenv(f"DBPORT")


def get_engine(dbname:str):
    """Function criacao de engine do banco de dados."""
    try:
        dbengine = sa.create_engine(f"postgresql+psycopg2://{DBUSER}:{DBPWD}@{DBHOST}:{DBPORT}/{dbname}")
    except Exception as e:
        print("Erro ao conectar com o db: ",e)
        dbengine = None
    return dbengine

def query_to_df(query:str,dbname:str):
    """Function to execute a query and return a dataframe."""
    try:
        dbengine = get_engine(dbname)
        with dbengine.connect() as cnt:
            df = pd_read_sql(sa.text(query),cnt)
    except Exception as e:
        print("Erro ao executar a query: ",e)
        df = None
    return df
