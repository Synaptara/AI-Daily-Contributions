def binary_search(sorted_list, target):
    # Initialize low and high pointers
    low = 0
    high = len(sorted_list) - 1

    # Continue search until low is less than or equal to high
    while low <= high:
        # Calculate mid index
        mid = (low + high) // 2

        # Check if target is found at mid index
        if sorted_list[mid] == target:
            return mid

        # If target is less than mid element, update high pointer
        elif sorted_list[mid] > target:
            high = mid - 1

        # If target is greater than mid element, update low pointer
        else:
            low = mid + 1

    # Return -1 if target is not found
    return -1


def main():
    # Example usage
    sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    result = binary_search(sorted_list, target)

    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the list")


if __name__ == "__main__":
    main()