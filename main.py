from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    


class TransportType(str, Enum):
    sms = "sms"
    email = "email"
    gchat = "gchat"

@app.get("/api/message/hello/{whom}")
async def hello(whom: str):
    return {"message": f"Hello {whom}"}

@app.get("/api/message/multihello/{count}")
async def multihello(count: int):
    return {"message": "HELLO" * count}

@app.get("/api/message/{messagetype}/{message}")
async def sendmessage(messagetype: TransportType, message: str,  signature: bool|None=None, priority: int=1):
    return {"message": f'Using {messagetype.value} to send {message} at priority {priority} {"using" if signature else "not using"} signature'}


@app.post("/api/items/")
async def create_item(item: Item):
    # add item to database after validation
    return item

# @app.post()
# @app.put()