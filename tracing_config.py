"""
Tracing Configuration - OpenTelemetry Setup
Integração com AI Toolkit para visualização de traces
"""

import os
import logging
from opentelemetry import trace, _events, _logs
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry.sdk._events import EventLoggerProvider
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.instrumentation.openai_v2 import OpenAIInstrumentor


def setup_tracing(service_name: str = "orchestrator_agent") -> None:
    """
    Configure OpenTelemetry tracing para o orchestrator_agent.
    
    Conecta ao AI Toolkit OTLP endpoint (localhost:4318) para visualização
    de traces e logs em tempo real.
    
    Args:
        service_name: Nome do serviço a aparecer nos traces
    """
    
    # Ativar captura de conteúdo de mensagens
    os.environ["OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT"] = "true"
    
    # Resource definition
    resource = Resource(attributes={
        "service.name": service_name,
        "service.version": "1.0.0",
        "deployment.environment": "development"
    })
    
    # Trace Provider Setup
    provider = TracerProvider(resource=resource)
    
    # OTLP Exporter para traces
    otlp_trace_exporter = OTLPSpanExporter(
        endpoint="http://localhost:4318/v1/traces",
    )
    trace_processor = BatchSpanProcessor(otlp_trace_exporter)
    provider.add_span_processor(trace_processor)
    trace.set_tracer_provider(provider)
    
    # Logger Provider Setup
    _logs.set_logger_provider(LoggerProvider())
    otlp_log_exporter = OTLPLogExporter(endpoint="http://localhost:4318/v1/logs")
    log_processor = BatchLogRecordProcessor(otlp_log_exporter)
    _logs.get_logger_provider().add_log_record_processor(log_processor)
    
    # Event Logger Setup
    _events.set_event_logger_provider(EventLoggerProvider())
    
    # Instrument OpenAI SDK
    OpenAIInstrumentor().instrument()
    
    logging.info(f"✅ OpenTelemetry tracing configured for: {service_name}")
    logging.info(f"📊 OTLP Endpoint: http://localhost:4318")
    logging.info(f"📊 View traces in AI Toolkit (cmd: ai-mlstudio.tracing.open)")


def get_tracer(name: str) -> trace.Tracer:
    """
    Get tracer instance para um módulo específico.
    
    Args:
        name: Nome do módulo/tracer
        
    Returns:
        Tracer instance
    """
    return trace.get_tracer(name)
