from sqlalchemy import Column, Integer, Float, String
from data.orm.mysql.DbUtils import *

Base = declarative_base()
session = get_session('spotify_music')

# Create a MySQL connection
conn = get_db_connection()
cursor = conn.cursor()

class Audio_Features(Base):
    __tablename__ = 'audio_features'

    track_feature_id = Column(String(500), primary_key=True, autoincrement=True)
    mode = Column(Integer)
    key = Column(Integer)
    duration = Column(Integer)
    tempo = Column(Float)
    time_signature = Column(Integer)

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

    @classmethod
    def create_instance(cls, row):
        instance = cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])

        instance.track_feature_id = row[0]

        return instance

    @classmethod
    def getExclusiveFeatures(cls):
        sql = """
            SELECT id, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, valence FROM audio_features
        """

        result_rows = cursor.execute(sql).fetchall()

        return [cls.create_instance(row) for row in result_rows]

    @classmethod
    def getAudioFeatures(cls):
        sql = """
            SELECT * FROM audio_features
        """


        result_rows = cursor.execute(sql).fetchall()

        return [cls.create_instance(row) for row in result_rows]