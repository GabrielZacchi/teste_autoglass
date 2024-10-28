from typing import Union

def multiply_numbers(num1: Union[int, str, float], num2: Union[int, str, float]) -> int:
    try:
        num1_int = int(num1)
        num2_int = int(num2)
        result = num1_int * num2_int
        return result
    except ValueError:
        raise ValueError("Error: Parameters must be numeric.")

if __name__ == "__main__":
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        result = multiply_numbers(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
    except Exception as e:
        print(str(e))