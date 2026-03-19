import logging
import os
from datetime import datetime
from pathlib import Path

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.log"

logs_path = Path(os.getcwd()) / "logs"
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = Path.joinpath(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
