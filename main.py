
import requests

from bs4 import BeautifulSoup as BS
from webscraping import *  
from flask import Flask, request

app = Flask(__name__)

@app.route('/operator')
def get_operator(): 
    operator = request.args['operator']
    operator = operator.lower()
    URL = 'https://www.ubisoft.com/en-us/game/rainbow-six/siege/game-info/operators/{}'.format(operator)
    print(URL)
    page = requests.get(URL)
    soup = BS(page.content, 'html.parser')
    return export_json(soup, operator)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

    


