import pandas as pd

def createColumns(disc_file):
    cols_to_create = ["pe", "eps", "ticker"]
    for c in cols_to_create:
        disc_file[c] = None
    return disc_file

def main():
    disc_file_name = "bank-nifty.csv"
    disc_file = pd.read_csv(disc_file_name)
    disc_file = createColumns(disc_file)
    disc_file.to_csv(disc_file_name, index=False)

main()
