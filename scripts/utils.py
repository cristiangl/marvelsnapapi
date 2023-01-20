import os
import requests
from PIL import Image

MARVEL_ZONE_CARDS_IMAGE_URL = "https://static.marvelsnap.pro/cards/"


def resize(imagePath):
        image = Image.open(imagePath)
        image = image.crop((125, 0, image.width - 125, image.height))
        image.save(imagePath, 'webp', optimize=True, quality=10)

def descargar_imagen(nombre, carpeta = 'images'):
    # Crear la carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    errores = []
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