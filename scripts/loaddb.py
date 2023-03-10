import requests
import json 
import re
import os
from utils import descargar_imagen
from pathlib import Path


MARVEL_ZONE_CARDS_URL = "https://static2.marvelsnap.pro/snap/do.php?cmd=getCards"
MARVEL_ZONE_CARDS_IMAGE_URL = "https://static.marvelsnap.pro/cards/"

print("\n\n")
print("=============================================")
print("| Actualizando base de datos de Marvel Snap |")
print("=============================================\n")
print("Conectando con Marvel Snap Zone...")

res = requests.get(MARVEL_ZONE_CARDS_URL)
response = json.loads(res.text)

IMAGE_FOLDER = Path(__file__).parents[1]
print(IMAGE_FOLDER)

print("\nConstruyendo la base de datos...")

cards = response

db = []
for cardID in cards:
    card = cards[cardID]
    card['description'] = re.sub(r'\<(.*?)\>', '', card['description'])
    card['image'] = '/images/'+ card['CardDefId'] + '.webp'

    if not os.path.exists(str(IMAGE_FOLDER) + '/images/'+ card['CardDefId'] + '.webp'):
        print('No existe => images/'+ card['CardDefId'] + '.webp')
        isImageSaved = descargar_imagen(card['CardDefId'])
        if not isImageSaved:
            continue

    card['abilities'] = json.loads(card['abilities'])
    card['collectible'] = int(card['collectible'])
    variantsData = json.loads(card['variants'])
    variants = []
    for varData in variantsData:
        if varData['id'] == 'base':
            continue
        
        varTemp = {}
        varTemp['id'] = varData['id']
        varTemp['credits'] = {}
        if 'credits' in varData:
            varTemp['credits'] = varData['credits']
        varTemp['image'] = '/images/' + card['CardDefId'] + '_' + varData['id'] + '.webp'

        if not os.path.exists(str(IMAGE_FOLDER) + '/images/' + card['CardDefId'] + '_' + varData['id'] + '.webp'):
            print('No existe => images/'+ card['CardDefId'] + '_' + varData['id'] + '.webp')
            isImageSaved = descargar_imagen(card['CardDefId'] + '_' + varData['id'])
            if not isImageSaved:
                continue

        variants.append(varTemp)
    
    card['variants'] = variants

    connectedCards = []
    connectedCardsData = json.loads(card['connected_cards'])
    for conData in connectedCardsData:
        conDataTemp = {}
        conDataTemp['id'] = conData
        conDataTemp['image'] = '/images/' + conData + '.webp'
        connectedCards.append(conDataTemp)

    card['connectedCards'] =  connectedCards
    del card['connected_cards']
    db.append(card)
    

f = open('db/database.json', 'w')

f.write(json.dumps(db))

print("\nLa base de datos de Marvel Snap, ??ha sido actualizada! \U0001f60E \U0001f389\n")