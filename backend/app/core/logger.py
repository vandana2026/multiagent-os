from pathlib import Path
from loguru import logger
import sys

# Logs folder
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Remove default logger
logger.remove()

# Console Logger
logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
           "<level>{message}</level>",
)

# File Logger
logger.add(
    LOG_DIR / "multiagent.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="DEBUG",
)

app_logger = logger