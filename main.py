# import libraries
import requests
from bs4 import BeautifulSoup as BS
from flask import Flask, request

# import module
from webscraping import export_json

# define Flask app
app = Flask(__name__)

# define GET method


@app.route('/operator', methods=["GET"])
def get_operator() -> list:
    operator = request.args['operator']
    operator = operator.lower()
    URL = 'https://www.ubisoft.com/en-us/game/rainbow-six/siege/game-info/operators/{}'.format(
        operator)
    page = requests.get(URL)
    soup = BS(page.content, 'html.parser')
    return export_json(soup)



