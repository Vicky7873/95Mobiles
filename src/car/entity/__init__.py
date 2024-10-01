from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class CarDataIngestionConfig:
    root_dir:Path
    download_uri: str
    raw_data_path: Path