def check_palindrome(input_value):
    # convert input to string for easier comparison
    input_str = str(input_value)
    # compare input string with its reverse
    return input_str == input_str[::-1]

def main():
    # example usage
    test_cases = ["radar", 12321, "python", 123456]
    for test_case in test_cases:
        print(f"{test_case} is palindrome: {check_palindrome(test_case)}")

if __name__ == "__main__":
    main()