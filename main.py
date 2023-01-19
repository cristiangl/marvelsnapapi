from typing import Union
import json
from utils.utils import *

from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def get():
    return 'Welcome Marvel Snap Api'

@app.get("/cards")
def getAllCards():
    try:
        return readDataBase()
    except Exception as e:
        return "Error: " + str(e)


@app.get("/card/{card_name}")
def getCard(card_name: str):

    try:
        cards = findCardInDB(card_name, readDataBase())

        if len(cards):
            return cards

        return {
            "status": "404",
            "message": "Carta " + card_name + " no encontrada"
        }
    except Exception as e:
        return "Error: " + str(e)