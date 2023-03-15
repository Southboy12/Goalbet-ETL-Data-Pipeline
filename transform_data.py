import pandas as pd
from extract_data import extract_data
from util import convert_to_datetime


def transform_data():
    df = pd.read_csv('data/league.csv')
    df['Date'] = pd.to_datetime(df.Date)
    print(df.info())
    df = convert_to_datetime(df, 'Date', '%d/%m/%Y')
    print(df.info)



transform_data()