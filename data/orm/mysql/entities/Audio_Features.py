from sqlalchemy import Column, Integer, Float, String
from data.orm.mysql.DbUtils import *

Base = declarative_base()
session = get_session('spotify_music')


class Audio_Features(Base):
    __tablename__ = 'audio_features'

    track_feature_id = Column(String(500), primary_key=True)
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

    def __init__(self, track_feature_id, mode, key, duration, tempo, time_signature,
                 acousticness, analysis_url, danceability, energy, instrumentalness,
                 liveness, loudness, speechiness, valence):
        self.track_feature_id = track_feature_id
        self.mode = mode
        self.key = key
        self.duration = duration
        self.tempo = tempo
        self.time_signature = time_signature
        self.acousticness = acousticness
        self.analysis_url = analysis_url
        self.danceability = danceability
        self.energy = energy
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.loudness = loudness
        self.speechiness = speechiness
        self.valence = valence

    @classmethod
    def create_table(cls):
        return

    @classmethod
    def create_instance(cls, row):
        instance = cls(
            track_feature_id=row.track_feature_id,
            mode=row.mode,
            key=row.key,
            duration=row.duration,
            tempo=row.tempo,
            time_signature=row.time_signature,
            acousticness=row.acousticness,
            analysis_url=row.analysis_url,
            danceability=row.danceability,
            energy=row.energy,
            instrumentalness=row.instrumentalness,
            liveness=row.liveness,
            loudness=row.loudness,
            speechiness=row.speechiness,
            valence=row.valence
        )

        return instance

    @classmethod
    def getExclusiveFeatures(cls):
        sql = """
            SELECT id, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, valence FROM audio_features
        """

        result_rows = session.query(cls).all()

        return [cls.create_instance(row) for row in result_rows]

    @classmethod
    def getAudioFeatures(cls):
        sql = session.query(cls)

        result_rows = session.query(cls).all()

        return [cls.create_instance(row) for row in result_rows]


results = Audio_Features.getAudioFeatures()