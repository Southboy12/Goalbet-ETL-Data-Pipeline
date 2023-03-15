import pandas as pd
from util import get_leaguedb_conn


def load_data():
    df = pd.read_csv('transformed/transformed_league_data.csv')
    engine = get_leaguedb_conn()
    df.to_sql('league_data', con=engine, if_exists='replace', index=False)
    print('Data successfully written to postgreSQL database')

