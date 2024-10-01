import pandas as pd
from IPython.display import display

def read_excel(path_file, name_spreadsheet):
    df = pd.read_excel(path_file, sheet_name=name_spreadsheet)

    return df

def show_data_excel(df):
    display(df)