from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class MobileDataIngestionConfig:
    root_dir: Path
    download_url: str
    mobile_raw_data: Path


@dataclass(frozen=True)
class Mobile_Data_Cleaning_Config:
    root_dir: Path
    mobile_raw_data: Path
    mobile_cleaned_data: Path



@dataclass(frozen=True)
class Mobile_fe_Config:
    root_dir: Path
    mobile_cleaned_data: Path
    final_data: Path