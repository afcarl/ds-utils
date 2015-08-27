import numpy as np


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