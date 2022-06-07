import yaml
import os
import shutil


def read_params(config_path:str)->dict:
    with open(config_path) as yaml_file:
        config= yaml.safe_load(yaml_file)

    return config

def clean_prev_dirs_if_exists(dir_path:str)->None:
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)

def create_dir(dirs:list)->None:
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok=True)

def save_file(uploaded_file):
    pass
