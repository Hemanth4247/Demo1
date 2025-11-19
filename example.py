import argparse

#!/usr/bin/env python3

def is_even(n: int) -> bool:
    return n % 2 == 0

def main():
    parser = argparse.ArgumentParser(description="Check if a number is even or odd")
    parser.add_argument("number", nargs="?", type=int, help="integer to check")
    args = parser.parse_args()

    if args.number is None:
        try:
            args.number = int(input("Enter an integer: ").strip())
        except ValueError:
            print("Invalid input: please enter an integer.")
            return

    n = args.number
    print(f"{n} is {'even' if is_even(n) else 'odd'}")

if __name__ == "__main__":
    main()