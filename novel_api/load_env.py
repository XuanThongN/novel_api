import subprocess
import json
import os
import logging
import time

from os.path import join
from pathlib import Path
from sys import platform
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def load_env():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    load_dotenv(os.path.join('backend', '.env'))

    # Load Secrets

    if os.environ.get('SECRET_KEY') is None:
        dotenv_path = join(os.path.dirname(base_dir), '.env')
        load_dotenv(dotenv_path)

    if os.environ.get('SECRET_KEY') is None:
        dotenv_path = Path("../.env")
        load_dotenv(dotenv_path=dotenv_path)


def write_env():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Write Secrets
    with open(join(os.path.dirname(base_dir), '.env'), "w") as f:
        for environment_key in os.environ:
            f.write(f"{environment_key}={os.environ.get(environment_key)}\n")


if __name__ == "__main__":
    write_env()
