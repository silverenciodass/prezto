from pathlib import Path
from os import environ


def filter_files(directory: Path):

  filtered = filter(lambda f: str(f)[0] == "z", directory.iterdir())

  return list(filtered)


def generate_name_files(list_of_files: list):

  mapper = map(lambda files: f".{files}", list_of_files)

  return list(mapper)


def create_links(file: Path, link: str, env, hard_link=False):

  l = Path(f"{env}/{link}")

  if hard_link:
    l.hardlink_to(file)
    print(f"{env}/{link} => {file.resolve()}")
  else:
    l.symlink_to(file)
    print(f"{env}/{link} -> {file.resolve()}")



this_dir = Path(".")

files = filter_files(this_dir)

links = generate_name_files(files)

c = 0

while c != len(files):
  create_links(files[c], links[c], environ["HOME"], True)
  c+=1
