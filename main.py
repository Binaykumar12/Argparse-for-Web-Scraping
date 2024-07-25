import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple argparse example")

# Add arguments
parser.add_argument('name', type=str, help="Your name")
parser.add_argument('age', type=int, help="Your age")
parser.add_argument('--greet', action='store_true', help="Print a greeting message")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"Hello, {args.name}! You are {args.age} years old.")
if args.greet:
    print("Nice to meet you!")
