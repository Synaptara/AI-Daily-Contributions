def largest_integer(s):
    # sort digits in descending order to form the largest possible integer
    digits = sorted(s, reverse=True)
    # join sorted digits into a single string and convert to integer
    return int(''.join(digits))

def main():
    # example usage
    print(largest_integer("531"))

if __name__ == "__main__":
    main()