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


@dataclass(frozen=True)
class CarDatSPlitConfig:
    root_dir: Path
    clean_data: Path
    X_train: Path
    X_test: Path
    y_train: Path
    y_test: Path
    test_size: float
    random_state: int



@dataclass(frozen=True)
class CarModelConfig:
    root_dir: Path
    X_train: Path
    X_test: Path
    y_train:Path
    y_test: Path
    model_save: Path
    model_for_train: Path
    fit_intercept: list[bool]
    n_estimators: list [int]
    criterion: list[str]
    bootstrap: list[bool]
    oob_score: list[bool]
    splitter: list[str]
