import asyncio
import logging
from fastapi import HTTPException, status
import requests
import random
from opentelemetry import trace
from opentelemetry.trace.status import Status, StatusCode
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
# from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter  # Changed to HTTP exporter

from opentelemetry.sdk.resources import Resource

import requests
from fastapi import FastAPI

random.seed(54321)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/ping")
async def health_check():
    return "pong"


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    if item_id % 2 == 0:
        # mock io - wait for x seconds
        seconds = random.uniform(0, 3)
        await asyncio.sleep(seconds)
    return {"item_id": item_id, "q": q}


# @app.get("/invalid")
# async def invalid():
#     raise ValueError("Invalid ")

@app.get("/exception")
async def exception():
    try:
        raise ValueError("sadness")
    except Exception as ex:
        logger.error(ex, exc_info=True)
        span = trace.get_current_span()

        # generate random number
        seconds = random.uniform(0, 30)

        # record_exception converts the exception into a span event. 
        exception = IOError("Failed at " + str(seconds))
        span.record_exception(exception)
        span.set_attributes({'est': True})
        # Update the span status to failed.
        span.set_status(Status(StatusCode.ERROR, "internal error"))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Got sadness")

@app.get("/external-api")
def external_api():
    seconds = random.uniform(0, 3)
    response = requests.get(f"https://httpbin.org/delay/{seconds}")
    response.close()
    return "ok"


# Configure OpenTelemetry
# tracer = trace.get_tracer(__name__)
trace_provider = TracerProvider(
    resource=Resource.create({"service.name": "my-sample-fastapi-service"})
)
# trace.set_tracer_provider(trace_provider)
span_exporter = OTLPSpanExporter(
    endpoint="http://localhost:4318/v1/traces", # SigNoz OTel Collector endpoint (gRPC)
    # endpoint="http://135.224.170.18:4318/v1/traces",
)
span_processor = BatchSpanProcessor(span_exporter)
trace_provider.add_span_processor(span_processor)

FastAPIInstrumentor.instrument_app(app=app, tracer_provider=trace_provider)