import os
import sys
from pathlib import Path
from log import logger


list_of_dirs = [
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/mobiles/__init__.py",
    f"src/mobiles/constants/__init__.py",
    f"src/mobiles/utils/__init__.py",
    f"src/mobiles/utils/common.py",
    f"src/mobiles/components/__init__.py",
    f"src/mobiles/config/__init__.py",
    f"src/mobiles/config/configuration.py",
    f"src/mobiles/pipelines/__init__.py",
    "src/mobiles/entity/__init__.py",
    "config/mobiles_config.yaml",
    "params/mobiles_params.yaml",
    "dvc.yaml",
    "setup.py",
    "research/mobiles/trials.ipynb",
    "templates/mobile_index.html",

    # this for Bike

    f"src/bike/__init__.py",
    f"src/bike/constants/__init__.py",
    f"src/bike/utils/__init__.py",
    f"src/bike/utils/common.py",
    f"src/bike/components/__init__.py",
    f"src/bike/config/__init__.py",
    f"src/bike/config/configuration.py",
    f"src/bike/pipelines/__init__.py",
    "src/bike/entity/__init__.py",
    "config/bike_config.yaml",
    "params/bike_params.yaml",
    "research/bike/trials.ipynb",
    "templates/bike_index.html",

    # this is for car

    f"src/car/__init__.py",
    f"src/car/constants/__init__.py",
    f"src/car/utils/__init__.py",
    f"src/car/utils/common.py",
    f"src/car/components/__init__.py",
    f"src/car/config/__init__.py",
    f"src/car/config/configuration.py",
    f"src/car/pipelines/__init__.py",
    "src/car/entity/__init__.py",
    "config/car_config.yaml",
    "params/car_params.yaml",
    "research/car/trials.ipynb",
    "templates/car_index.html",

    # this is for laptop

    f"src/laptop/__init__.py",
    f"src/laptop/constants/__init__.py",
    f"src/laptop/utils/__init__.py",
    f"src/laptop/utils/common.py",
    f"src/laptop/components/__init__.py",
    f"src/laptop/config/__init__.py",
    f"src/laptop/config/configuration.py",
    f"src/laptop/pipelines/__init__.py",
    "src/laptop/entity/__init__.py",
    "config/laptop_config.yaml",
    "params/laptop_params.yaml",
    "research/laptop/trials.ipynb",
    "templates/laptop_index.html",

]

for dir_path in list_of_dirs:
    files = Path(dir_path)
    files.parent.mkdir(parents=True, exist_ok=True)
    if not files.exists():
        with open(files, 'w') as f:
            pass
        logger.info(f"Created {files} completed")

