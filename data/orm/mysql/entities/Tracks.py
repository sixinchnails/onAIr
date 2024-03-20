from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base
from data.orm.mysql.DbUtils import *

Base = declarative_base()
session = get_session('spotify_music')

# Create a MySQL connection
# conn = get_db_connection()
# cursor = conn.cursor()

class Tracks(Base):
    __tablename__ = 'tracks'

    track_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500))
    artist = Column(String(500))
    duration = Column(Integer)
    disc_number = Column(Integer)
    explicit = Column(Integer)
    preview_url = Column(String(500))
    track_number = Column(Integer)
    popularity = Column(Float, nullable=False)
    is_playable = Column(Integer)
    album_cover_url = Column(String(500))
    music_url = Column(String(500))

    @classmethod
    def create_instance(cls, row):
        instance = cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])

        instance.id = row[0]

        return instance

    @classmethod
    def create_popularity_instance(cls, row):
        instance = cls(row[1])

        instance.id = row[0]

        return instance

    @classmethod
    def getTracks(cls):
        sql = "SELECT * FROM tracks"

        result_rows = cursor.execute(sql).fetchall()

        return [cls.create_instance(row) for row in result_rows]

    @classmethod
    def getPopularity(cls):
        sql = "SELECT id, popularity from tracks"

        result_rows = cursor.execute(sql).fetchall()

        return [cls.create_popularity_instance(row) for row in result_rows]