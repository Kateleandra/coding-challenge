from datetime import date


def get_file_name() -> str:
    base_dir = "/tmp"
    file_name = f"{date.today().isoformat().replace('-','')}.txt"
    file = f"{base_dir}/{file_name}"

    return file


def update_file(line: str) -> None:
    file = get_file_name()
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{line}\n")
