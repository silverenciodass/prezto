from pathlib import Path
from os import environ


def filter_files(directory: Path):

  filtered = filter(lambda f: str(f)[0] == "z", directory.iterdir())

  return list(filtered)


def generate_name_files(list_of_files: list):

  mapper = map(lambda files: f".{files}", list_of_files)

  return list(mapper)


this_dir = Path(".")

files = filter_files(this_dir)

links = generate_name_files(files)
