#!/home/vijay/anaconda3/bin/python

import pandas as pd
from os.path import dirname, abspath, join

def get_data(files, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    dfstocks = pd.DataFrame(index=dates)
    if 'NIFTY.csv' not in files:  # add NIFTY for reference, if absent
        files.insert(0, 'NIFTY.csv')

    data_dir = join(dirname(dirname(abspath(__file__))), "data")

    for f in files:
        # TODO: Read and join data for each symbol
        files_path = join(data_dir, f)
        df_temp = pd.read_csv(files_path, index_col = "Date", 
                           parse_dates = True,
                           usecols = ['Date', 'Close Price'])
        df_temp = df_temp.rename(columns = {'Close Price' : f})
        dfstocks = dfstocks.join(df_temp, how = 'inner')