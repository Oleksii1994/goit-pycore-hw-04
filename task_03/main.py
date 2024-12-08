import sys
from pathlib import Path
from colorama import init, Fore, Style
from directory_structure import print_directory_structure

def main() -> None:
    """
    Main function to execute the script. It reads the directory path from
    command line arguments and prints its structure.
    """
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python main.py /path/to/directory{Style.RESET_ALL}")
        sys.exit(1)
    
    directory_path = Path(sys.argv[1])
    
    if not directory_path.exists():
        print(f"{Fore.RED}Error: The path '{directory_path}' does not exist.{Style.RESET_ALL}")
        sys.exit(1)
    
    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: The path '{directory_path}' is not a directory.{Style.RESET_ALL}")
        sys.exit(1)
    
    print(f"Structure of directory '{directory_path}':")
    print_directory_structure(directory_path)

if __name__ == '__main__':
    init(autoreset=True)
    main()