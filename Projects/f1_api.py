# data.nba.net/prod/v1/today.json

from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://f1api.dev/api"
ALL_JSON = "/teams"

printer = PrettyPrinter()
data = get(BASE_URL + ALL_JSON).json()
printer.pprint(data)
