from contextlib import asynccontextmanager

from fastapi import FastAPI


def fake_answer_to_everything_ml_model(x: float):
    return 42

ml_models = {}


# this decorator converts the function into an "async context manager" (can be used in a "with" statement)
@asynccontextmanager  
async def lifespan(app: FastAPI):
    print("Setting up before `yield`...")
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    print("Cleaning up after `yield`...")
    ml_models.clear()
    
app = FastAPI(lifespan=lifespan)

@app.get("/predict")
async def predict(x: float):
    result = ml_models["answer_to_everything"](x)
    return {"prediction": result}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "lifespan:app",
        host="0.0.0.0",  # Allow external connections
        port=6666,       # Default FastAPI port
        reload=True      # Auto-reload on code changes
    )