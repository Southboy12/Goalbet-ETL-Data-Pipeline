import pandas as pd



def convert_to_datetime(df, column_name, date_format):
    """
    Convert a date column in a Pandas DataFrame from object to datetime.

    Parameters:
    df (Pandas DataFrame): the DataFrame containing the date column
    column_name (str): the name of the date column to convert
    date_format (str): the format of the date column (e.g. '%d/%m/%Y')

    Returns:
    The modified DataFrame with the date column converted to datetime.
    """
    df[column_name] = pd.to_datetime(df[column_name], format=date_format)
    return df

   
