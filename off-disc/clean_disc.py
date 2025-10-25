import pandas as pd


def clean_columns(disc_file):
    disc_file.columns = disc_file.columns.str.lower().str.strip()
    disc_file[["eps", "pe"]] = (
        pd.NA
    )  # These are the only metrics supported by =GOOGLEFINANCE. Do not create symbol column as it will create merge errors
    return disc_file
