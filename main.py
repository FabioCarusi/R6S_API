# import libraries
import requests

# import modules
from flask import Flask, request
from tinydb import TinyDB
from bs4 import BeautifulSoup as BS
from settings import OPERATORS
from dbquery import get_all_operators, get_side_detail, get_squad_detail, insert_table, get_operator

DB = TinyDB('r6s_db.json')
TABLE = DB.table('operators')

# define flask app
app = Flask(__name__)

# scaping method


def scraping_page(op: str) -> any:
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    URL = 'https://www.ubisoft.com/en-us/game/rainbow-six/siege/game-info/operators/{}'.format(
        op)
    page = requests.get(URL, headers=headers)
    return BS(page.content, 'html.parser')

# POST methods


@app.route('/add_all_operators', methods=['POST'])
def add_all_operators():
    if len(TABLE.all()) == 0:
        for operator in OPERATORS:
            operator = operator.lower()
            soup = scraping_page(operator)
            insert_table(soup, operator, TABLE)
    else:
        return "One or more operators are already present", 400


@app.route('/add_new_operator', methods=['POST'])
def add_new_operator():
    op = request.args['operator']
    soup = scraping_page(op)
    insert_table(soup, op, TABLE)

# get methods


@app.route('/get_operator')
def operator():
    op = request.args['operator']
    op_detail = get_operator(op, TABLE)

    return op_detail


@app.route('/get_all_operator')
def all_operator():
    return get_all_operators(TABLE)


@app.route('/get_squad_members')
def squad_members():
    squad = request.args['squad']
    squad_detail = get_squad_detail(squad, TABLE)

    return squad_detail


@app.route('/get_side')
def side_members():
    side = request.args['side']
    side_detail = get_side_detail(side, TABLE)

    return side_detail
