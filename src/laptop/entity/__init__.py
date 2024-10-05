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



@dataclass(frozen=True)
class Laptop_datasplit:
    root_dir: Path
    laptop_cleaned_data: Path
    X_train: Path
    X_test: Path
    y_train: Path
    y_test: Path
    test_size: float
    random_state: int

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    X_train: Path
    X_test: Path
    y_train: Path
    y_test: Path
    saved_model: Path
    model_for_train: Path


@dataclass(frozen=True)
class laptop_modelevalconfig:
    root_dir: Path
    X_train: Path
    X_test: Path
    y_train: Path
    y_test: Path
    save_score: Path
    model_for_train: Path