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


@dataclass(frozen=True)
class DatasplitConfig:
    root_dir: Path
    feature_eng_data: Path
    X_train: Path
    X_test: Path
    y_train: Path
    y_test: Path
    test_size: float
    random_state: int

@dataclass(frozen=True)
class BikeModelTuningConfig:
    root_dir: Path
    X_train: Path
    X_test: Path
    y_train: Path
    y_test: Path
    tunned_model: Path
    n_estimators: int
    bootstrap: bool
    criterion: str
    oob_score: bool
    mlflow_uri: str