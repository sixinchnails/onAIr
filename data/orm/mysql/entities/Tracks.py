from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base
from data.orm.mysql.DbUtils import *

Base = declarative_base()
session = get_session('spotify_music')

# Create a MySQL connection
conn = get_db_connection()
cursor = conn.cursor()

class Tracks(Base):
    __tablename__ = 'tracks'

    feature_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False)
    artist = Column(String(500), nullable=False)
    duration = Column(Integer, nullable=False)
    disc_number = Column(Integer, nullable=False)
    explicit = Column(Integer, nullable=False)
    audio_feature_id = Column(String(500), nullable=False)
    preview_url = Column(String(500))
    track_number = Column(Integer, nullable=False)
    popularity = Column(Float, nullable=False)
    is_playable = Column(Integer, nullable=False)
    album_cover_url = Column(String(500), nullable=False)
    music_url = Column(String(500), nullable=False)