import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Dict, List, Union, Optional, Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: returns ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file loaded from: {path_to_yaml} successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Yaml file is empty: {path_to_yaml}")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create list of directories

    Args:
        path_to_directories (list): list of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Default to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path:Path, data:dict):
    """
    save json data
    Args:
        path (Path): path to save json file
        data (dict): data to be saved in json file
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"saved json file at: {path}")

@ensure_annotations
def load_json(path:Path):
    """
    load json data
    Args:
        path (Path): path to json file
    """

    with open(path, "r") as f:
        content = json.load(f)
    
    logger.info(f"loaded json file from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path:Path):
    """
    save binary data
    Args:
        data (Any): data to be saved
        path (Path): path to save binary file
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"saved binary file at: {path}")

@ensure_annotations
def load_bin(path:Path):
    """
    load binary data
    Args:
        path (Path): path to binary file
    """

    data = joblib.load(filename=path)
    logger.info(f"loaded binary file from: {path}")
    return data

@ensure_annotations
def get_size(path:Path) ->str:
    """
    get size in KB
    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"

@ensure_annotations
def decodeImage(imgstring, filename):
    """
    decode image from base64 string
    Args:
        imgstring (str): base64 string

    Returns:
        image: decoded image
    """

    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

@ensure_annotations
def encodeImageBase64(croppedImage):
    with open(croppedImage, "rb") as img_file:
        return base64.b64encode(img_file.read())
    