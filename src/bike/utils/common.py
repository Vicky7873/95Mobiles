import os
from box.exceptions import BoxValueError
import yaml
from ensure import ensure_annotations # type: ignore
from box import ConfigBox
from pathlib import Path
from typing import Any
from log import logger

def read_yaml(path_to_yaml:Path) -> ConfigBox:
    with open(path_to_yaml) as file:
        content = yaml.safe_load(file)
        logger.info(f"yaml: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
    
def create_directory(list_of_dirs:list,verbose=True):
    for path in list_of_dirs:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
