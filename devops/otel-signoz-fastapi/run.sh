# Load environment variables from .env file
if [ -f .env ]; then
  export $(cat .env | xargs)
fi


OTEL_RESOURCE_ATTRIBUTES=service.name=example-fastapi-signoz-app \
OTEL_EXPORTER_OTLP_ENDPOINT="ingest.us.signoz.cloud:443" \
OTEL_EXPORTER_OTLP_HEADERS="signoz-access-token=${SIGNOZ_ACCESS_TOKEN}" \
OTEL_EXPORTER_OTLP_PROTOCOL=grpc \
opentelemetry-instrument uvicorn app.main:app --host localhost --port 5002