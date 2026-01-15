"""
Logging Configuration - Robust logging setup
Logs estruturados para arquivo e console com níveis configuraáveis
"""

import logging
import logging.handlers
import json
from pathlib import Path
from datetime import datetime
from typing import Optional


class JSONFormatter(logging.Formatter):
    """Formatter que output logs em formato JSON estruturado"""
    
    def format(self, record: logging.LogRecord) -> str:
        log_obj = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        # Adicionar exception info se presente
        if record.exc_info:
            log_obj["exception"] = self.formatException(record.exc_info)
        
        # Adicionar extra fields se presentes
        if hasattr(record, "extra_fields"):
            log_obj.update(record.extra_fields)
        
        return json.dumps(log_obj, ensure_ascii=False)


class PlainFormatter(logging.Formatter):
    """Formatter legível para console output"""
    
    FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    
    def __init__(self):
        super().__init__(self.FORMAT, self.DATE_FORMAT)


def setup_logging(
    log_dir: Optional[Path] = None,
    console_level: int = logging.INFO,
    file_level: int = logging.DEBUG,
    service_name: str = "orchestrator_agent"
) -> logging.Logger:
    """
    Configura logging robusto com múltiplos handlers.
    
    Args:
        log_dir: Diretório para guardar logs (default: logs/)
        console_level: Nível de logging para console
        file_level: Nível de logging para ficheiros
        service_name: Nome do serviço para prefixo de logs
        
    Returns:
        Logger instance configurada
    """
    
    # Setup log directory
    if log_dir is None:
        log_dir = Path("logs")
    else:
        log_dir = Path(log_dir)
    
    log_dir.mkdir(exist_ok=True, parents=True)
    
    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    
    # Remove existing handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Console Handler (plain text, human readable)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(PlainFormatter())
    root_logger.addHandler(console_handler)
    
    # File Handler - All logs (JSON format)
    all_logs_file = log_dir / f"{service_name}_all.log"
    file_handler = logging.handlers.RotatingFileHandler(
        all_logs_file,
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5,
        encoding="utf-8"
    )
    file_handler.setLevel(file_level)
    file_handler.setFormatter(JSONFormatter())
    root_logger.addHandler(file_handler)
    
    # File Handler - Errors only
    error_logs_file = log_dir / f"{service_name}_errors.log"
    error_handler = logging.FileHandler(
        error_logs_file,
        encoding="utf-8"
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(JSONFormatter())
    root_logger.addHandler(error_handler)
    
    # Get service logger
    logger = logging.getLogger(service_name)
    logger.setLevel(logging.DEBUG)
    
    # Log startup info
    logger.info(f"✅ Logging configured for: {service_name}")
    logger.info(f"📝 All logs: {all_logs_file}")
    logger.info(f"🔴 Error logs: {error_logs_file}")
    logger.info(f"Console level: {logging.getLevelName(console_level)}")
    logger.info(f"File level: {logging.getLevelName(file_level)}")
    
    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get logger instance para um módulo específico.
    
    Args:
        name: Nome do módulo/logger
        
    Returns:
        Logger instance
    """
    return logging.getLogger(name)


def log_with_context(logger: logging.Logger, level: int, message: str, **context) -> None:
    """
    Log com contexto adicional (extra fields).
    
    Args:
        logger: Logger instance
        level: Log level (logging.INFO, logging.ERROR, etc)
        message: Log message
        **context: Extra fields para incluir no log
    """
    extra = {"extra_fields": context} if context else {}
    logger.log(level, message, extra=extra)
