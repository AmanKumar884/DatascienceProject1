# Import required modules
import os                    # For creating directories and checking file existence
from pathlib import Path     # For handling paths in a cross-platform way
import logging               # For logging actions instead of print statements

# Set up logging format and level
logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s]: %(message)s:'
)

# Define the base project name (used for creating structured folders)
project_name = "datascience"

# Define all the files and folders we want to create for our project
list_of_files = [
    ".gthub/workflows/.gitkeep",                           # Keeps .github folder in version control even if empty
    f"src/{project_name}/__init__.py",                     # Marks 'src/datascience' as a Python package
    f"src/{project_name}/components/__init__.py",          # Marks 'components' as a subpackage
    f"src/{project_name}/utils/__init__.py",               # Marks 'utils' as a subpackage
    f"src/{project_name}/utils/common.py",                 # Common utility functions
    f"src/{project_name}/config/__init__.py",              # Marks 'config' as a subpackage
    f"src/{project_name}/config/configuration.py",         # Configuration logic (like reading YAMLs)
    f"src/{project_name}/pipeline/__init__.py",            # Pipeline package (training, evaluation etc.)
    f"src/{project_name}/entity/__init__.py",              # Entity classes (like DataIngestionConfig)
    f"src/{project_name}/entity/config_entity.py",         # Custom classes for config schema
    f"src/{project_name}/constants/__init__.py",           # For storing constant values like file paths
    "config/config.yaml",                                  # Project configuration in YAML format
    "params.yaml",                                         # Hyperparameters file
    "schema.yaml",                                         # Data schema definition
    "main.py",                                             # Main execution script
    "Dockerfile",                                          # Container configuration file
    "setup.py",                                            # Setup script for packaging
    "research/research.ipynb",                             # Jupyter notebook for exploration
    "templates/index.html",                                # Web front-end template (for Flask or Streamlit)
    "app.py"                                               # Flask/FastAPI app entry point
]

# Loop through each file path
for filepath in list_of_files:
    filepath = Path(filepath)                       # Convert to a Path object (cross-platform safety)
    filedir, filename = os.path.split(filepath)     # Split into directory and file name

    # Create the directory if it doesn't already exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)         # Creates the directory if needed
        logging.info(f"Creating directory {filedir} for the file : {filename}")
    
    # Create the file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass                                    # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    
    # If the file already exists and has content, log that info
    else:
        logging.info(f"{filename} already exists")
