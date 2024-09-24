import logging
import os
import sys

log_dir = "logs"
log_path = os.path.join(log_dir, "log.txt")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s",
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)   

logger = logging.getLogger("95Mobiles")

logger.info("Logging file start")

