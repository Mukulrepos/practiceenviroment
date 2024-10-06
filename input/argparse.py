import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="This program displays the square of a given number.")

# Add an argument for the number
parser.add_argument("num", type=int, help="Please input an integer number")

# Parse the arguments
args = parser.parse_args()

# Calculate and print the square of the number
result = args.num ** 2
print(f"The square of {args.num} is {result}")
