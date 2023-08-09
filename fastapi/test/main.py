from typing import Union

from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet  = "resnet"
    lenet   = "lenet"

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()


@app.get("/") # python 데코레이터
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name" : model_name, "message" : "Deep Learning FTW!"}
    
    if model_name.value == 'lenet':
        return {"model_name" : model_name, "message" : "LeCNN all the images"}
    
    return {"model_name" : model_name, "message" : "Have some residuals"}
