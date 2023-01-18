from typing import Union
from utils import *

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get():
    return 'Welcome Marvel Snap Api'

@app.get("/cards")
def getAllCards():
    return readDataBase()


@app.get("/card/{card_name}")
def getCard(card_name: str):

    cards = findCardInDB(card_name, readDataBase())

    if len(cards):
        return cards

    return {
        "status": "404",
        "message": "Carta " + card_name + " no encontrada"
    }