from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base
from data.orm.mysql.DbUtils import *

Base = declarative_base()
session = get_session('spotify_music')

# Create a MySQL connection
conn = get_db_connection()
cursor = conn.cursor()

class Audio_Features(Base):
    __tablename__ = 'audio_features'

    feature_id = Column(String(500), primary_key=True, autoincrement=True)
    mode = Column(Integer, nullable=False)
    key = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    tempo = Column(Float, nullable=False)
    time_signature = Column(Integer, nullable=False)

    # Features used in Regression
    acousticness = Column(Float, nullable=False)
    analysis_url = Column(String(500), nullable=False)
    danceability = Column(Float, nullable=False)
    energy = Column(Float, nullable=False)
    instrumentalness = Column(Float, nullable=False)
    liveness = Column(Float, nullable=False)
    loudness = Column(Float, nullable=False)
    speechiness = Column(Float, nullable=False)
    valence = Column(Float, nullable=False)