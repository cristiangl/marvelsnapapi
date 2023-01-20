import os
import requests
from utils.utils import readDataBase
import PIL
from PIL import Image

MARVEL_ZONE_CARDS_IMAGE_URL = "https://static.marvelsnap.pro/cards/"

def resize(imagePath):
        image = Image.open(imagePath)
        image = image.crop((125, 0, image.width - 125, image.height))
        image.save(imagePath, 'webp', optimize=True, quality=10)

def descargar_imagenes(nombres, carpeta):
    # Crear la carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    errores = []
    for nombre in nombres:
        print(nombre)
        # Construir la URL de la imagen
        url = MARVEL_ZONE_CARDS_IMAGE_URL + str(nombre) + '.webp'
        # Descargar la imagen
        try:
            response = requests.get(url)
            # Guardar la imagen en la carpeta
            fileName = carpeta + "/" + nombre + '.webp'
            with open(fileName, "wb") as f:
                f.write(response.content)
            
            resize(fileName)
        except:
            errores.append(url + "no encontrada")
    
    for error in errores:
        print(error)
        
        

cards = readDataBase()

cardNames = []

for card in cards:
    cardNames.append(card['CardDefId'])
    variantsName = []

    for var in card['variants']:
        cardNames.append(card['CardDefId'] + "_" + var['id'])

descargar_imagenes(cardNames, 'images')

