from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/{item_id}")
async def create_item(item: Item, item_id: int):
    item_dict: dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"item_id": item_id, "price_with_tax": price_with_tax})
    return item_dict


if __name__ == "__main__":
    # run the server
    # then run `node request-body.js` in the terminal to send a request 
    import uvicorn

    uvicorn.run("request-body:app", host="127.0.0.1", port=8000, reload=True)
