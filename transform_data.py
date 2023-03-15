import pandas as pd
from util import convert_to_datetime


def transform_data():
    df = pd.read_csv('extract/league.csv')
    df['Date'] = pd.to_datetime(df.Date, dayfirst=True)
    df = convert_to_datetime(df, 'Date', '%d/%m/%y')
    df.to_csv('transformed/transformed_league_data.csv', index=False)
    print('Data successfully transformed and written to csv file')

