from tinydb import TinyDB, Query
import webscraping as ws
from settings import OPERATORS


db = TinyDB('r6s_db.json')
table = db.table('operators')

operators_db = []

for item in table:
    operators_db.append(item['Name'])

operators_list = OPERATORS

for el in operators_db:
    for l in operators_list:
        if el == l:
            operators_db.remove(el)
            operators_list.remove(l)

print(operators_list) 