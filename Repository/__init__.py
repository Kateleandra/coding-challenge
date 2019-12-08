from datetime import date
from os import walk, system


def exist(base_dir: str, file_name: str) -> bool:
    # r=root, d=directories, f = files
    for r, d, f in walk(base_dir):
        for file in f:
            if file == file_name:
                return True
        return False


def create_file() -> str:
    base_dir = "/tmp"
    file_name = f"{date.today().isoformat().replace('-','')}.txt"
    file = f"{base_dir}/{file_name}"

    if not exist(base_dir, file_name):
        print(f"creating file {file}...")
        system(f"touch {file}")

    return file


def update_file(line: str) -> None:
    file = create_file()
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{line}\n")
