import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess_movies(df):
    df = df.dropna()
    return df
