from datetime import date


def get_file_name() -> str:
    """Return file name in '/tmp/YYYYMMDD.txt' format."""
    base_dir = "/tmp"
    file_name = f"{date.today().isoformat().replace('-','')}.txt"
    file = f"{base_dir}/{file_name}"

    return file


def update_file(line: str) -> None:
    """Input data into a new line in the current date file"""
    file = get_file_name()
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{line}\n")


def read_file() -> list:
    """Returns current date file content"""
    file = get_file_name()

    with open(file, "r") as file:
        return file.readlines()
