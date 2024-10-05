from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class LaptopDataIngestionConfig:
    root_dir: Path
    download_url: str
    laptop_raw_data: Path


@dataclass(frozen=True)
class Laptop_feConfig:
    root_dir: Path
    laptop_raw_data: Path
    laptop_cleaned_data: Path