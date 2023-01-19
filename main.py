from typing import Union
import json
from utils.utils import *
from starlette.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get():
    return 'Welcome Marvel Snap Api'

@app.get("/cards")
def getAllCards():
    try:
        return JSONResponse(status_code=200, content={"data": readDataBase()})
    except Exception as e:
        return JSONResponse(status_code=404, content={"message": "Error: " + str(e)})

@app.get("/cards/{search}")
def getFilteredCards(search: str):
    try:
        cards = searchCardsInDB(search, readDataBase())

        if len(cards):
            return JSONResponse(status_code=200, content={"data": cards}) 

        return JSONResponse(status_code=404, content={"message": "Carta " + search + " no encontrada"})
    except Exception as e:
        return "Error: " + str(e)

@app.get("/card/{card_name}")
def getCard(card_name: str):

    try:
        card = findCardInDB(card_name, readDataBase())

        if card:
            return JSONResponse(status_code=200, content={"data": card}) 

        return JSONResponse(status_code=404, content={"message": "Carta " + card_name + " no encontrada"})
    except Exception as e:
        return "Error: " + str(e)