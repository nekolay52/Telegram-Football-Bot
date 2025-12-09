from bs4 import BeautifulSoup
from config import proxies
import requests


def started_matches():
    url = "https://onefootball.com/en/matches?only_live=true"
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, features="html.parser")

    matches = soup.find_all('div', class_="SimpleMatchCard_simpleMatchCard__content__ZWt2p")

    end = ""

    for i in matches:
        es = {}

        team = i.find_all('span', class_="SimpleMatchCardTeam_simpleMatchCardTeam__name__7Ud8D")
        team1 = es["team1"]=team[0].text
        team2 = es["team2"]=team[1].text

        score = (i.find_all('span', class_="SimpleMatchCardTeam_simpleMatchCardTeam__score__UYMc_"))
        score1 = es["score1"]=score[0].text
        score2 = es["score2"]=score[1].text

        time = (i.find('span', class_="title-8-bold SimpleMatchCard_simpleMatchCard__live__kg0bW"))
        half_team = (i.find('span', class_="title-8-medium SimpleMatchCard_simpleMatchCard__infoMessage___NJqW SimpleMatchCard_simpleMatchCard__infoMessage__secondary__hisY4"))

        if time == None:
            time = half_team.text
        if half_team == None:
            time = time.text

        end = end + f"{team1} {score1} - {score2} {team2} ~ {time}\n\n"
    return end
