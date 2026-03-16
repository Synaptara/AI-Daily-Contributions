def binary_to_decimal(binary_string):
    decimal = 0
    # initialize power of 2
    power = 0
    # iterate from the end of the string to the beginning
    for char in reversed(binary_string):
        # if the character is '1', add the corresponding power of 2 to the decimal
        if char == '1':
            decimal += 2 ** power
        # increment the power for the next iteration
        power += 1
    return decimal

def main():
    binary_string = "1010"
    print(binary_to_decimal(binary_string))

if __name__ == "__main__":
    main()