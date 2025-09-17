# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Draw the Pattern
row = 0
while row < size:
    for col in range(size):
        print("*", end="")  # print stars side by side
    print()  # move to the next line after one row
    row += 1
