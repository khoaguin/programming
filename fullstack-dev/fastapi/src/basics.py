from fastapi import FastAPI
from enum import Enum

app = FastAPI()


### Path Parameters ###
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Because path operations are evaluated in order, you need to make sure that the path for 
# /users/me is declared before the one for /users/{user_id}
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")  # `:path` declares a path parameter
async def read_file(file_path: str):
    # file_path can contains paths home/dk/myfile.txt
    # so, the URL for that file would be: /files/home/dk/myfile.txt.
    return {"file_path": file_path}


#### Query Parameters ####
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")  # e.g. http://127.0.0.1:8000/items/?skip=1&limit=10
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# @app.get("/items2/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

@app.get("/items2/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")  # e.g. http://127.0.0.1:8000/users/1/items/9?q=a&short=false
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "basics:app", 
        host="localhost", 
        port=8000, 
        reload=True
    )