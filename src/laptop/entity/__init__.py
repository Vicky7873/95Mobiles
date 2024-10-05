from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class LaptopDataIngestionConfig:
    root_dir: Path
    download_url: str
    laptop_raw_data: Path