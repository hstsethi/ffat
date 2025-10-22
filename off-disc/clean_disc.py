import pandas as pd
def createColumns(disc_file):
    disc_file[["eps", "pe"]] = pd.NA # Do not create symbol column as it will create merge errors
    return disc_file

def cleanColumns(disc_file):
    disc_file.columns = disc_file.columns.str.lower().str.strip()
    return disc_file

