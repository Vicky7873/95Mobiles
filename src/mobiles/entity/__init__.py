from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class MobileDataIngestionConfig:
    root_dir: Path
    download_url: str
    mobile_raw_data: Path