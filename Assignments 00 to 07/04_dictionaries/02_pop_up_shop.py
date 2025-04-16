# Problem Statement
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):

# How many (apple) do you want?: 2

# How many (durian) do you want?: 0

# How many (jackfruit) do you want?: 1

# How many (kiwi) do you want?: 0

# How many (rambutan) do you want?: 1

# How many (mango) do you want?: 3

# Your total is $99.5





def main():
    fruit_prices = {
        "apple": 3.5,
        "durian": 15.0,
        "jackfruit": 25.0,
        "kiwi": 2.5,
        "rambutan": 4.0,
        "mango": 8.0
    }

    total_cost = 0.0

    for fruit, price in fruit_prices.items():
        quantity_str = input(f"How many ({fruit}) do you want?: ")
        quantity = int(quantity_str)
        total_cost += price * quantity

    print(f"\nYour total is ${total_cost}")

if __name__ == '__main__':
    main()
