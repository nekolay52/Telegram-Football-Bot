from bs4 import BeautifulSoup
from config import proxies
import datetime
import requests


def upcoming_match(url):
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, features="html.parser")

    match = soup.find_all('div', class_="XpaLayout_xpaLayoutContainerGridItemComponents__MaerZ")
    match2 = match[1].find('div', class_="SimpleMatchCard_simpleMatchCard__teamsContent__vSfWK")
    match3 = match2.find_all('span')

    time1 = match[1].find('div', class_="SimpleMatchCard_simpleMatchCard__matchContent__prwTf")
    time2 = time1.find('time')["datetime"]
    time3 = datetime.datetime.strptime(time2, "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(hours=1)

    end = time3.strftime("%d.%m.%Y\n  %H:%M")+ f"\n{match3[0].text} - {match3[2].text}\n\n"
    return end
