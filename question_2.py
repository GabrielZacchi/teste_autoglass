from typing import List

def show_even_numbers(numbers: List[int]) -> None:
    try:
        if not all(isinstance(num, int) for num in numbers):
            raise ValueError("All elements must be integers.")
        
        even_numbers = [num for num in numbers if num % 2 == 0]
        print("Even numbers:", even_numbers)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    show_even_numbers(numbers)