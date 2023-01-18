import json


def readDataBase ():

    f = open('db/database.json')

    data = json.load(f)

    return data

def findCardInDB(searchName, db):
    results = []
    searchNameCleared = searchName.lower().strip()
    for card in db:
        if card['name'].lower().startswith(searchNameCleared):
            results.append(card)
    
    return results