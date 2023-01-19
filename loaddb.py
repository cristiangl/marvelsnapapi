import requests
import json 
import re

MARVEL_ZONE_CARDS_URL = "https://marvelsnapzone.com/getinfo/?searchtype=cards&searchcardstype=true"

def pascal_to_kebab(string):
    string = re.sub(r'[^\w-]', '-', string)
    string = re.sub(r'([A-Z])', lambda x: '-' + x.group(1).lower(), string)
    string = re.sub(r'--', '-', string)
    string = re.sub(r'^-*|-*$', '', string)
    return string
print("\n\n")
print("=============================================")
print("| Actualizando base de datos de Marvel Snap |")
print("=============================================\n")
print("Conectando con Marvel Snap Zone...")

res = requests.get(MARVEL_ZONE_CARDS_URL)
response = json.loads(res.text)

print("\nConstruyendo la base de datos...")

cards = response['success']['cards']

db = []
for card in cards:
    name = card['carddefid']
    if name == '':
        name = card['name'].replace(" ", "")

    card['name-slug'] = pascal_to_kebab(name)
    db.append(card)

f = open('db/database.json', 'w')

f.write(json.dumps(db))

print("\nLa base de datos de Marvel Snap, ¡ha sido actualizada! \U0001f60E \U0001f389\n")