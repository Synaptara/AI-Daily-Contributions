def factorial_recursive(n):
    # base case: factorial of 0 is 1
    if n == 0:
        return 1
    # recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)

def factorial_loop(n):
    # initialize result variable to 1
    result = 1
    # loop from 1 to n, multiplying result by each number
    for i in range(1, n+1):
        result *= i
    return result

def main():
    n = 5  # example input
    print(f"Factorial of {n} (recursive): {factorial_recursive(n)}")
    print(f"Factorial of {n} (loop): {factorial_loop(n)}")

if __name__ == "__main__":
    main()