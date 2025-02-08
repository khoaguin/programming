from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class RPCStatusCode(Enum):
    NOT_FOUND = "RPC_NOT_FOUND"
    PENDING = "RPC_PENDING"
    COMPLETED = "RPC_COMPLETED"
    ERROR = "RPC_ERROR"


class ItemResponse(BaseModel):
    id: str
    status: RPCStatusCode
    items: Union[Item, list[Item]]


app = FastAPI()


@app.post("/items/{item_id}")
async def create_item(item: Item, item_id: int):
    item_dict: dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    item_response = ItemResponse(
        id=str(item_id), 
        status=RPCStatusCode.COMPLETED,
        items=Item(**item_dict)
    )
    return item_response


if __name__ == "__main__":
    # run the server
    # then run `node client.js` in the terminal to send a request 
    import uvicorn

    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
