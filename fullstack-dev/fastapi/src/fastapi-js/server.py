from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict
from enum import Enum
from typing import Optional
from datetime import datetime


class Base(BaseModel):
    """Base model with enhanced serialization capabilities."""

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={
            datetime: lambda dt: dt.isoformat(),
        },
        ser_json_bytes="base64",  #  encode any bytes fields as base64 strings during serialization
        val_json_bytes="base64",  # 
    )


class Item(Base):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    body: Optional[bytes] = None


class RPCStatusCode(Enum):
    NOT_FOUND = "RPC_NOT_FOUND"
    PENDING = "RPC_PENDING"
    COMPLETED = "RPC_COMPLETED"
    ERROR = "RPC_ERROR"


class ItemResponse(Base):
    id: str
    status: RPCStatusCode
    items: Union[Item, list[Item]]


app = FastAPI()


@app.post("/items/{item_id}")
async def create_item(item: Item, item_id: int):
    item_dict: dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax, "body": b"hello world"})
    item_response = ItemResponse(
        id=str(item_id), 
        status=RPCStatusCode.COMPLETED,
        items=[Item(**item_dict), Item(**item_dict)]
    )
    import pdb; pdb.set_trace()
    return JSONResponse(content=item_response.model_dump(model="json"))


if __name__ == "__main__":
    # run the server
    # then run `node client.js` in the terminal to send a request 
    import uvicorn

    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
