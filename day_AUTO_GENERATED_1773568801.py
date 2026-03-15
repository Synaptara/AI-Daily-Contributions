def largest_number(n):
    # convert integer into list of digits
    digits = [int(x) for x in str(n)]
    # sort digits in descending order
    digits.sort(reverse=True)
    # join digits to form largest number and convert back to integer
    return int(''.join(map(str, digits)))

def main():
    n = 42145
    print(largest_number(n))

if __name__ == "__main__":
    main()