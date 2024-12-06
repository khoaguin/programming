import time
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource

# Step 1: Configure the OTLP Exporter
exporter = OTLPSpanExporter(
    endpoint="http://135.224.170.18/v1/traces",  # Root URL for your SigNoz setup
)

# Step 2: Set up a Tracer Provider and Span Processor
tracer_provider = TracerProvider(
    resource=Resource.create({"service.name": "my-sample-fastapi-service"})
)
span_processor = BatchSpanProcessor(exporter)
tracer_provider.add_span_processor(span_processor)
trace.set_tracer_provider(tracer_provider)

# Step 3: Create a Tracer
tracer = trace.get_tracer(__name__)

# Step 4: Generate a Test Trace
print("Starting a test trace...")
with tracer.start_as_current_span("test-span") as span:
    span.set_attribute("test_key", "test_value")
    span.add_event("Test Event", {"event_key": "event_value"})
    time.sleep(1)  # Simulate some work
print("Test trace completed!")

# Step 5: Cleanup
span_processor.shutdown()