from tinydb import TinyDB, Query, where


db = TinyDB('r6s_db.json')
table = db.table('operators')
op = Query()

result = table.search(op['Name'] == 'brava')
print(result)
#('Squad') == 'Wolfguard')
#for r in result:
 #   print(r['Name'])

#table.truncate()
""" for item in table:
    print(item['Name']) """
