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

@dataclass(frozen=True)
class mobile_datasplitconfig:
    root_dir: Path
    X_train: Path
    X_test: Path
    y_train:Path
    y_test: Path
    final_data: Path
    test_size: float
    random_state: int


@dataclass(frozen=True)
class mobile_Modeltrainconfig:
    root_dir: Path
    X_train: Path
    X_test: Path
    y_train:Path
    y_test: Path
    save_model: Path
    model_for_train: Path



@dataclass(frozen=True)
class mobile_model_eval_config:
    root_dir: Path
    X_train: Path
    X_test: Path
    y_train:Path
    y_test: Path
    model_for_train: Path
    save_score: Path