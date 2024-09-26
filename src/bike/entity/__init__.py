from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Bike_DataIngestionConfig:
    root_dir: Path
    download_url: str
    bike_raw_data: Path


@dataclass(frozen=True)
class Bike_feature_engg:
    root_dir: Path
    bike_raw_data: Path
    feature_eng_data: Path