from typing import Tuple

def total_salary(path: str) -> Tuple[int, int]:
    """
    Calculates the total and average salary of developers from a file.

    Args:
        path (str): The path to the text file containing salary data.

    Returns:
        Tuple[int, int]: A tuple containing two integers:
            - Total sum of all salaries.
            - Average salary of developers.
    """
    total = 0
    count = 0
    
    try:
        # open the file for reading
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # remove whitespace and split the line into name and salary
                parts = line.strip().split(',')
                                
                if len(parts) == 2:
                    # convert the salary to an integer
                    try:
                        salary = int(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        print(f"Warning: Invalid salary format '{parts[1]}' in line '{line}'")
    
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return (0, 0)
    except Exception as e:
        print(f"An error occurred: {e}")
        return (0, 0)
    
    # calculate the average salary
    average = total // count if count > 0 else 0
    
    return (total, average)

def main():
    file_path = 'task_01/salaries.txt'
    result = total_salary(file_path)
    print(f"Total salary sum: {result[0]}, Average salary: {result[1]}")
    
if __name__ == '__main__':
    main()