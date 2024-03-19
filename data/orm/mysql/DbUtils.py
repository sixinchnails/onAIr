import pymysql, configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read('config.ini')
user = config['DB']['user']
password = config['DB']['password']
server_ip = config['DB']['serverIP']
db = config['DB']['db']


def initialize_session(db_name):
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{server_ip}/{db_name}")

    base = declarative_base()
    base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)

    return session()


def get_db_connection():
    conn = pymysql.connect(
        host=server_ip,
        user=user,
        password=password,
        db=db
    )

    conn.autocommit = True

    return conn


def get_session(db_name):
    return initialize_session(db_name)
