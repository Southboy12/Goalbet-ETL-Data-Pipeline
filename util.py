import pandas as pd
import dotenv
from sqlalchemy import create_engine
import os



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
    df[column_name] = pd.to_datetime(df[column_name], date_format)
    return df
   

def get_leaguedb_conn():
    dotenv.load_dotenv('C:/Users/MENKA/Downloads/My-project/Environment files/.env')
    db_user_name = os.getenv('LEAGUE_DB_USER_NAME')
    db_password = os.getenv('LEAGUE_DB_PASSWORD')
    db_name = os.getenv('LEAGUE_DB_NAME')
    port = os.getenv('LEAGUE_PORT')
    host = os.getenv('LEAGUE_HOST')
    return create_engine(f'postgresql+psycopg2://{db_user_name}:{db_password}@{host}:{port}/{db_name}')
