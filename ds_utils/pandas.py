import numpy as np
import pandas as pd


def dataframe_size(df):
    """Return a dict with the size of DataFrame components in MB.
    :param df: pandas.DataFrame
    :return dictionary with index, columns, values and total size
    """
    byte_to_megabyte_factor = 1024 ** 2
    size = dict(zip(['index', 'columns', 'values'],
                    np.array([df.index.nbytes, df.columns.nbytes,
                              df.values.nbytes]) / byte_to_megabyte_factor))
    size['total'] = np.sum(size.values())
    return size
    
def print_full(df):
    """Print the full DataFrame  
    
    :param df: pandas.DataFrame
    :return None
    
    See: 
    - http://stackoverflow.com/questions/19124601/is-there-a-way-to-pretty-print-the-entire-pandas-series-dataframe
    """
    with pd.option_context('display.max_rows', len(df), 'display.max_columns', len(df.shape[1])):
        print df
