import pandas as pd


def map_symbols_to_isin(disc_file, isin_db):
    merged = pd.merge(disc_file, isin_db, on="isin")
    return merged
