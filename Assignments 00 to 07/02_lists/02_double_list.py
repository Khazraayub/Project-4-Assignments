# Problem Statement
# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]


def double_numbers(nums: list[int]) -> list[int]:
    """
    Doubles each number in the list and returns the new list.
    """
    doubled: list[int] = []
    for num in nums:
        doubled.append(num * 2)
    return doubled

def main():
    numbers: list[int] = [1, 2, 3, 4]
    result: list[int] = double_numbers(numbers)
    print("Doubled numbers:", result)

if __name__ == '__main__':
    main()
