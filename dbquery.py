import webscraping as ws
import re
from settings import OPERATORS
from tinydb import Query, where

Operators = Query()


def insert_table(soup: any, op: str, table: any):
    info = ws.info_operator(soup, op)
    loadouts = ws.loadout(soup)
    bio_info = ws.biography_info(soup)
    bio = ws.biography(soup)

    data = info | loadouts | bio_info | bio

    if table.search(Operators.Name == op):
        return f'{op} founds', 200
    else:
        table.insert(data)
        return f'New operator inserts: {op}', 200


def get_operator(op: str, table: any)-> dict:
    detail_op = table.search(Operators['Name'].matches(op, re.IGNORECASE))

    if len(detail_op) == 0:
        return f'Operator {op} not found', 400
    else:
        return detail_op


def get_all_operators(table: any) -> dict:
    result = table.all()

    if len(result) == 0:
        return 'Database empty', 400
    else:
        return result


def get_squad_detail(squad: str, table: any)-> list:
    squad_detail = table.search(
        Operators['Squad'].matches(squad, re.IGNORECASE))

    squad_list = []

    if len(squad_detail) == 0:
        return f'Squad {squad} not found', 400
    else:
        for s in squad_detail:
            squad_list.append(s['Name'])

    return squad_list
    
def get_side_detail(side: str, table: any) -> list:
    side_detail = table.search(
        Operators['Side'].matches(side, re.IGNORECASE))
    
    side_list = []

    if len(side_detail) == 0:
        return f'Side {side} not found', 404
    else:
        for s in side_detail:
            side_list.append(s['Name'])
    
    return side_list


