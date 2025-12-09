from bs4 import BeautifulSoup
from config import proxies
import requests


def match_results(url):
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, features="html.parser")

    match_cards = soup.find_all('div', class_="SimpleMatchCard_simpleMatchCard__content__ZWt2p")

    end = ""

    for card in match_cards:
        team = card.find_all('span', class_="SimpleMatchCardTeam_simpleMatchCardTeam__name__7Ud8D")
        team1 = team[0].text
        team2 = team[1].text

        score = card.find_all('span', class_="SimpleMatchCardTeam_simpleMatchCardTeam__score__UYMc_")
        score1 = score[0].text
        score2 = score[1].text

        time = card.find('div', class_="SimpleMatchCard_simpleMatchCard__matchContent__prwTf")
        time1 = time.text.replace("Full time", " ")

        end = end + f"{team1} {score1} - {score2} {team2}\n{time1}\n\n"
    return end
