import pandas as pd
from get_links import get_links

data = []
def extract_data():
    links = get_links()
    for link in links:
        # I removed Time column because it's not in the last csv file
        df = pd.read_csv(link, usecols=['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])
        data.append(df)
    df = pd.concat(data, axis=0, ignore_index=True)
    df.to_csv('data/league.csv', index=False)
