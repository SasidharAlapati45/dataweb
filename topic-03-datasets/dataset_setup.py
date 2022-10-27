import dataset

db = dataset.connect('sqlite:///shopping_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'Mangoes' },
        { "description": 'PBM' },
        { "description": 'garlicPizza' },
        { "description": 'Cookies' },
        { "description": 'IceCream' }
        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()
