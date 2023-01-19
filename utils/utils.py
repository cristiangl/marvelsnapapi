import json
from os.path import dirname, abspath, join, realpath
from pathlib import Path
dir = Path(__file__).parent.parent

def readDataBase ():
    f = open(join(dir, 'db', 'database.json'), 'r')

    data = json.load(f)

    return data

def findCardInDB(searchName, db):
    results = []
    searchNameCleared = searchName.lower().strip()
    for card in db:
        if card['name'].lower().startswith(searchNameCleared):
            results.append(card)
    
    return results