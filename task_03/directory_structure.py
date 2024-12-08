from pathlib import Path
from colorama import Fore, Style

def print_directory_structure(directory: Path, prefix: str = '') -> None:
    """
    Recursively prints the structure of the given directory.

    Args:
        directory (Path): The directory to print the structure of.
        prefix (str): The prefix to use for each line of output.

    The function uses the following syntax to visualize the directory tree:
    - '|-- ' is used to indicate a node that has subsequent nodes.
    - '|__ ' is used to indicate the last node at the current level.

    Examples:
        root/
        |-- dir1/
        |   |-- file1.txt
        |   |__ file2.txt
        |__ dir2/
            |__ file3.txt

    This helps in visually representing the hierarchy and structure of directories.
    """
    items = list(directory.iterdir())
    
    for index, path in enumerate(items):
        # set pointer based on whether it's the last item in the list
        pointer = '|__ ' if index == len(items) - 1 else '|-- '
        
        if path.is_dir():
            print(f"{prefix}{pointer}{Fore.BLUE}{path.name}{Style.RESET_ALL}")
            # update the prefix for the next level
            new_prefix = prefix + ('    ' if index == len(items) - 1 else '|   ')
            print_directory_structure(path, new_prefix)
        else:
            print(f"{prefix}{pointer}{Fore.GREEN}{path.name}{Style.RESET_ALL}")