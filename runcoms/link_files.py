from pathlib import Path
from os import environ


def filter_files(directory: Path):

  filtered = filter(lambda f: str(f)[0] == "z", directory.iterdir())

  return list(filtered)


this_dir = Path(".")

files = filter_files(this_dir)


