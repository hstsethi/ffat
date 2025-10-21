import pandas as pd
def mapSymbolsToISIN(disc_file, isin_db):
    merged = pd.merge(disc_file, isin_db, on="isin")
    return merged


