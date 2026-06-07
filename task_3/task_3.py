import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def parse_folder(path: Path, indent: str = ""):
    try:
        items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        for item in items:
            if item.is_dir():
                print(f"{indent}📂 {Fore.BLUE}{Style.BRIGHT}{item.name}")
                parse_folder(item, indent + "    ")
            else:
                print(f"{indent}📜 {Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[Доступ обмежено]")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Будь ласка, вкажіть шлях до директорії.")
        return

    dir_path = Path(sys.argv[1])

    if not dir_path.exists() or not dir_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях не існує або не є директорією.")
        return

    print(f"📦 {Fore.CYAN}{Style.BRIGHT}{dir_path.name}")
    parse_folder(dir_path, " ┣ ")

if __name__ == "__main__":
    main()