from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Bike_DataIngestionConfig:
    root_dir: Path
    download_url: str
    bike_raw_data: Path