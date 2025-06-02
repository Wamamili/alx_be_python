# Multiplication table - Generates and prints the multiplication table for a given number using a for loop.

def main():
    try:
        # user input
        number = int(input("Enter a number to see its multiplication table: "))

        # Generate and print the multiplication table from 1 to 10
        for i in range(1, 11):
            product = number * i
            print(f"{number} * {i} = {product}")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()