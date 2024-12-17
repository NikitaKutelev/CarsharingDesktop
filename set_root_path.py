"""
Module for initializing the project root path and configuring the environment.

"""
import os
import sys

from loguru import logger


def initialize_environment():
    """
    Initializes the environment by loading variables from the .env file
    and setting up the PYTHONPATH.
    """

    # Get the directory of the current file
    current_file_dir = os.path.dirname(os.path.abspath(__file__))

    # Move up to the project root directory
    project_root = os.path.abspath(
        os.path.join(current_file_dir, "..")
    )  # Move up one level

    # Add to sys.path if not already present
    if project_root not in sys.path:
        sys.path.append(project_root)
        logger.debug(f"Added {project_root} to PYTHONPATH.")

    os.environ["PYTHONPATH"] = project_root
    logger.debug(f"Environment initialized successfully at {project_root}.")


initialize_environment()
