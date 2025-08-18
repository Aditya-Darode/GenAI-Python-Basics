'''
Print a Centered Star Pyramid
Given an integer rows, print a centered pyramid of stars with rows number of rows. Each row should have spaces on the left so that the pyramid is symmetric.'''

# Function to print a centered star pyramid
def print_pyramid(rows):
    
    for i in range(rows):
        # Print spaces before the stars
        for j in range(rows - i - 1):
            print(" ", end="")  # end="" keeps printing in the same line

        # Print stars for the current row
        for j in range(2 * i + 1):
            print("*", end="")  # print stars side by side

        # Move to the next line after finishing current row
        print()

# Example usage
rows = 5
print_pyramid(rows)
