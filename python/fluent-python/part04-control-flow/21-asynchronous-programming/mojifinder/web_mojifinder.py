from pathlib import Path
from unicodedata import name

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from charindex import InvertedIndex

STATIC_PATH = Path(__file__).parent.absolute() / 'static'  # path of the `/static` dir

app = FastAPI(  # defines the ASGI app
    title='Mojifinder Web',  # app's title metadata
    description='This app helps you search for Unicode characters by name.',  # app's metadata
)

class CharName(BaseModel):
    """
    A pydantic schema for a JSON response with `char` and `name` fields
    """
    char: str
    name: str

def init(app: FastAPI):
    """
    Build the index and load the static HTML form, 
    attaching both to the `app.state` for later use
    """
    app.state.index = InvertedIndex()
    app.state.form = (STATIC_PATH / 'form.html').read_text()

init(app)  # Run init when this module is loaded by the ASGI server

'''Note:
The `init` and `form` functions used to load and serve the static
HTML form are a hack to make the example short and easy to run.
The recommended best practice is to have a proxy/load-balancer in
front of the ASGI server to handle all static assets, and also use a
CDN (Content Delivery Network) when possible. One such proxy/
load-balancer is Traefik, a self-described “edge router” that
“receives requests on behalf of your system and finds out which
components are responsible for handling them.” 
FastAPI has project generation scripts (https://fastapi.tiangolo.com/project-generation/)
that prepare your code to do that.
'''

@app.get('/search', response_model=list[CharName])  # Route for the `/search` endpoint; `response_model` uses that `CharName` pydantic model to describe the response format
async def search(q: str):
    """
    Args: 
        FastAPI assumes that any parameters that appear in the function or coroutine
        signature that are not in the route path will be passed in the HTTP query string,
        e.g., /search?q=cat. Since q has no default, FastAPI will return a 422 (Unpro‐
        cessable Entity) status if q is missing from the query string.
    Return:
        An iterable of dicts compatible with the `response_model` schema
        allows FastAPI to build the JSON response according to the `response_model` in
        the `@app.get` decorator. We can see that we defined `response_model=list[CharName]`,
        However, we return a generator of dict items, not a list of CharName
        objects, but that’s good enough for FastAPI and pydantic to validate the data and
        build the appropriate JSON response compatible with response_model=list[CharName]
    """
    chars = sorted(app.state.index.search(q))
    result = ({'char': c, 'name': name(c)} for c in chars)
    return result

@app.get('/', response_class=HTMLResponse, include_in_schema=False)
def form():  # Non-async functions can also be used to produce responses.
    return app.state.form

# This module has no main function. It is loaded and driven by
# the ASGI server (uvicorn in this example)
# We can see that this module has no direct calls to `asyncio`. 
# FastAPI is built on the Starlette ASGI toolkit, which in turn uses `asyncio`.