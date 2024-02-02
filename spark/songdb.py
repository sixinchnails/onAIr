import sqlite3, time, configparser
from sklearn.decomposition import PCA
import pandas as pd, pickle as pk
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)

config = configparser.ConfigParser()
config.read('config.ini')

pre_hdfs_input = config['SPARK']['pre_hdfs_input']

final_df = pd.read_csv(pre_hdfs_input)

neg_scaler = MinMaxScaler(feature_range=(-1, 1))
pos_scaler = MinMaxScaler(feature_range=(0, 1))

cols_to_exclude = pd.DataFrame()
cols_to_exclude['id'] = final_df['id']

cols_to_exclude['popularity'] = pd.DataFrame(
    pos_scaler.fit_transform(final_df['popularity'].values.reshape(-1, 1)))

exc_song_df = final_df.drop('id', axis=1).drop('popularity', axis=1)

scaled_songs_df = pd.DataFrame(neg_scaler.fit_transform(exc_song_df), columns=exc_song_df.columns)

pca = PCA(n_components=0.95)
pca_transformed = pca.fit_transform(scaled_songs_df)
pk.dump(pca, open("pca.pkl", "wb"))
pca_transformed_df = pd.DataFrame(pca_transformed)

pca_transformed_df['id'] = cols_to_exclude['id']
pca_transformed_df['popularity'] = cols_to_exclude['popularity']

#Re-arrange columns, so that 'id' comes first.
cols = pca_transformed_df.columns.tolist()
cols = cols[-1:] + cols[:-1]
cols = cols[-1:] + cols[:-1]
pca_transformed_df = pca_transformed_df[cols]

# Create a mapping dictionary for column renaming
column_mapping = {
    'id': 'audio_feature_id'
}

# Iterate through numerical columns and rename them to 'feat_x'
for i, col in enumerate(pca_transformed_df.columns):
    if type(col) is int:
        new_col_name = 'feat_' + str(col)
        column_mapping[col] = new_col_name

pca_transformed_df.rename(columns=column_mapping, inplace=True)

hdfs_input = config['SPARK']['hdfs_input']

pca_transformed_df.to_csv(hdfs_input, sep=',', index=False)
