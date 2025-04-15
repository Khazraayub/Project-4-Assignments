# Problem Statement
# Write a function that takes a list of numbers and returns the sum of those numbers.


def calculate_total(values: list[int]) -> int:
    """
    Returns the total sum of the given list of integers.
    """
    result: int = 0
    for val in values:
        result += val
    return result


def main():
    my_numbers: list[int] = [10,40,78,9,7]
    total: int = calculate_total(my_numbers)
    print(f"The sum is: {total}")

if __name__ == '__main__':
    main()
