import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]: %(message)s:')

project_name="cnn-classifer"

list_of_files= [".github/workflows/.gitkeep",
                f"src/{project_name}/__init__.py",
                f"src/{project_name}/components/__init__.py",
                f"src/{project_name}/utils/__init__.py",
                f"src/{project_name}/config/configurations.py",
                f"src/{project_name}/pipeline/__init__.py",
                f"src/{project_name}/entity/__init__.py",
                f"src/{project_name}/constants/__init__.py",
                "config/config.yaml",
                "dvc.yaml",
                "params.yaml",
                "requirements.txt",
                "setup.py",
                "research/trials.ipynb"]



for filepath in list_of_files:
    # Path(filepath) will automatically convert the path to windows path
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir != "":
        # is the file already exist, then there would not be any overriding or replacing of the original file
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")

    if(not os.path.exists(filepath) or os.path.getsize(filepath)):
        # this will create the file if it does not exist. So, when you use with open(filepath, "w") as f:, 
        # you're opening the file specified by filepath in write mode, and making it accessible within the 
        # context of the with block with the name f. After the with block finishes executing, the file is 
        # automatically closed. This is a recommended way to handle file operations in Python because it 
        # ensures proper handling of resources and prevents potential issues like leaving files open 
        # inadvertently.
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} already exists")