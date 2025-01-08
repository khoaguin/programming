1. To start the local cluster, do `just start-signoz` 
2. Run the OTel Collector:
```bash
OTEL_RESOURCE_ATTRIBUTES="service.name=$(hostname)" LOG_FILE_PATH="/home/dk/Desktop/projects/OpenMined/SyftBox/.server/data/logs/server.log" otelcol-contrib --config ./custom-otel-collector-config.yaml
```
3. Instrumenting the FastAPI to send data to the right endpoint, e.g.
```python
exporter = OTLPSpanExporter(endpoint="http://localhost:5555")
     span_processor = BatchSpanProcessor(exporter)
``` 
4. Run the FastAPI server and a client to send requests to the server to generate traces. For example, with SyftBox, we can run the server with `SYFTBOX_OTEL_ENABLED=1 just rs` and the client with `just rc a`.