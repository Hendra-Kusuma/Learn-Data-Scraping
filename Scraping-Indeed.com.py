import requests
import os
from bs4 import BeautifulSoup

url = 'https://id.indeed.com/jobs?'
params = {
    'q' : 'laravel developer',
    'l' : 'Jakarta'
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
}

res = requests.get(url, params=params, headers=headers)
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())


def Get_Total_Pages():
    params = {
        'q' : 'laravel developer',
        'l' : 'Jakarta'
    }

    res = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()
# Scraping Step
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.prettify())


if __name__ == '__main__':
    Get_Total_Pages()