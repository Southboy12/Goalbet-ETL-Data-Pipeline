import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import re


base_url = 'https://www.football-data.co.uk/'
# Extract Layer
def get_links():
    url = 'https://www.football-data.co.uk/englandm.php'
    response = requests.get(url)
    if response.status_code != 200:
        print(f'{url} returned an error {response.status_code}')
    else:
        page_content = response.text
        doc = bs(page_content, 'html.parser')
        a_tags = doc.find_all('a')
        links = []
        for a_tag in a_tags:
            href = a_tag.get('href')
            pattern = r'mmz4281/(1920/(E0|E2)|0203/E1)\.csv'
            match = re.search(pattern, href)
            if match:
                link = base_url + str(match.group())
                links.append(link)
            else:
                pass
        return links
            
            

        

docv = get_links()
docv