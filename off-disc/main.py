import pandas as pd
from map_symbols import map_symbols_to_isin
from clean_disc import clean_columns


def main():
    disc_file_name = "bank-nifty-ffat.xlsx"
    isin_db_name = "nse-isin.csv"
    isin_db = pd.read_csv(isin_db_name)
    disc_file = pd.read_excel(disc_file_name)
    disc_file = clean_columns(disc_file)
    disc_file = map_symbols_to_isin(disc_file, isin_db)
    disc_file.to_excel(disc_file_name, index=False)


main()
