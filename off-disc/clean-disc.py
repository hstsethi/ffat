import pandas as pd

def createColumns(disc_file):
    disc_file[["eps", "pe", "ticker"]] = pd.NA
    return disc_file

def cleanColumns(disc_file):
    disc_file.columns = disc_file.columns.str.lower().str.strip()
    return disc_file

def main():
    disc_file_name = "bank-nifty-ffat.xlsx"
    disc_file = pd.read_excel(disc_file_name)
    disc_file = cleanColumns(disc_file)
    # disc_file = createColumns(disc_file)
    disc_file.to_excel(disc_file_name, index=False)

main()
