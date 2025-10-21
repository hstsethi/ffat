import pandas as pd

def createColumns(disc_file):
    disc_file[["eps", "pe", "symbol"]] = pd.NA
    return disc_file

def cleanColumns(disc_file):
    disc_file.columns = disc_file.columns.str.lower().str.strip()
    return disc_file

def mapSymbolsToISIN(disc_file, isin_db):
    merged = pd.merge(disc_file, isin_db, on="isin")
    return merged

def main():
    disc_file_name = "bank-nifty-ffat.xlsx"
    isin_db_name = "nse-isin.csv"
    isin_db = pd.read_csv(isin_db_name)
    disc_file = pd.read_excel(disc_file_name)
    disc_file = cleanColumns(disc_file)
    disc_file = createColumns(disc_file)
    disc_file = mapSymbolsToISIN(disc_file, isin_db)
    disc_file.to_excel(disc_file_name, index=False)

main()
