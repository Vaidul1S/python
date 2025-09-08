# data.nba.net/prod/v1/today.json

from requests import get
from pprint import PrettyPrinter
from nba_api.stats.endpoints import scoreboard

BASE_URL = "https://f1api.dev/api"
ALL_JSON = "/teams"

response = get(BASE_URL + ALL_JSON).json()
games = scoreboard.ScoreBoard().json()
print(games)