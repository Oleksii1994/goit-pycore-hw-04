from typing import List, Dict

def get_cats_info(path: str) -> List[Dict[str, str]]:
    """
    Reads a file containing cat information and returns a list of dictionaries for each cat.

    Args:
        path (str): The path to the text file containing cat data.

    Returns:
        List[Dict[str, str]]: A list of dictionaries, each containing information about a cat.
    """
    cats_info = []
    
    try:
        # open the file for reading
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # remove whitespace, split the line into id, name, and age
                parts = line.strip().split(',')
                
                if len(parts) == 3:
                    # create a dictionary for the cat
                    cat_info = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats_info.append(cat_info)
    
    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return cats_info

def main():
    file_path = 'task_02/cats.txt'  
    cats_info = get_cats_info(file_path)
    print(cats_info)

if __name__ == '__main__':
    main()