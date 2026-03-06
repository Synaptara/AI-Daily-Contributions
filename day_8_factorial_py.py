def factorial_recursive(n):
    # base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # recursive case: n * factorial of (n-1)
    else:
        return n * factorial_recursive(n-1)

def factorial_loop(n):
    # initialize result variable to 1
    result = 1
    # loop from 2 to n (inclusive)
    for i in range(2, n+1):
        # multiply result by current number
        result *= i
    # return final result
    return result

def main():
    n = 5  # example input
    print("Factorial using recursion:", factorial_recursive(n))
    print("Factorial using loop:", factorial_loop(n))

if __name__ == "__main__":
    main()