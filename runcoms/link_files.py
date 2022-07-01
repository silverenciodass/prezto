from pathlib import Path
from os import environ

def filter_files(directory: Path):

  files = []

  for f in directory.iterdir():
    if str(f)[0] == "z":
      files.append(f)

  return files

this_dir = Path(".")

files = []


