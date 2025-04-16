# Problem: Planetary Weight Calculator
# Milestone #1: Mars Weight
# A few years ago, NASA made history with the first controlled flight on another planet. Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth. Interestingly, Ingenuity uses Python for some of its flight modeling software!

# Ingenuity on the surface of Mars (source: NASA)

# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

# The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.  

# Milestone #2: Adding in All Planets
# Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:






def mars_weight(earth_weight):
    mars_weight = round(earth_weight * 0.378, 2)
    print(f"Your weight on Mars would be: {mars_weight} kg")

def planetary_weight(earth_weight):
    gravity_factors = {
        "mercury": 0.38,
        "venus": 0.91,
        "mars": 0.38,
        "jupiter": 2.34,
        "saturn": 1.06,
        "uranus": 0.92,
        "neptune": 1.19,
        "pluto": 0.06
    }

    planet = input("Enter the name of a planet: ").strip().lower()
    if planet in gravity_factors:
        planet_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"Your weight on {planet.capitalize()} would be: {planet_weight} kg")
    else:
        print("Sorry, I don't have data for that planet.")

def main():
    print("🚀 Welcome to the Planetary Weight Calculator!")
    print("1. Calculate weight on Mars")
    print("2. Calculate weight on any planet")
    
    choice = input("Choose an option (1 or 2): ").strip()
    
    try:
        earth_weight = float(input("Enter your weight on Earth (kg): "))
        
        if choice == "1":
            mars_weight(earth_weight)
        elif choice == "2":
            planetary_weight(earth_weight)
        else:
            print("Invalid option. Please restart and choose 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number for your weight.")

if __name__ == "__main__":
    main()
