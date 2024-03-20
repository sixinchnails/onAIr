import pymysql, configparser
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

user = config['MYSQL']['user']
password = config['MYSQL']['password']
server_ip = config['MYSQL']['serverIP']

Base = declarative_base()

def initialize_session(db_name):
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{server_ip}/{db_name}")

    base = declarative_base()
    base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)

    return session()


def get_db_connection(db):
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


# sakila_session = initialize_session('sakila')
# actors = sakila_session.query(Actor).all()
#
# for actor in actors:
#     print(actor)
#
# sakila_session.close()
