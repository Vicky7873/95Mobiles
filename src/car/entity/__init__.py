from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class CarDataIngestionConfig:
    root_dir:Path
    download_uri: str
    raw_data_path: Path


@dataclass(frozen=True)
class CarFeatureEngConfig:
    root_dir: Path
    raw_data_path: Path
    clean_data: Path