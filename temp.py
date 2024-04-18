from plyer import notification
import requests
from bs4 import BeautifulSoup

url = "https://www.cricbuzz.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

team1 = None
team2 = None
team_elements = soup.find_all(class_="cb-col-50 cb-ovr-flo cb-hmscg-tm-name")
if team_elements:    
    team1 = team_elements[0].get_text()
    team2 = team_elements[1].get_text()
    print("Gotcha1")

team1_score = None
team2_score = None
if team1 and team2:
    team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
    team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()
    print("Gotcha2")

if team1_score is not None and team2_score is not None:
    print(f"{team1} : {team1_score}")
    print(f"{team2} : {team2_score}")
    print("Gotcha3")

    notification.notify(
        title="IPL SCORE",
        message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
        timeout=15
    )
else:
    print("Failed to retrieve team scores")
