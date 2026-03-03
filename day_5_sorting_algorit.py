def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Create a flag that will allow the function to terminate early if there's nothing left to sort
        swapped = False
        for j in range(0, n - i - 1):
            # Compare the adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap them if they're in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps were made, the list is sorted
        if not swapped:
            break
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the first element is the smallest
        min_index = i
        for j in range(i + 1, n):
            # Check if there's a smaller element
            if arr[j] < arr[min_index]:
                # Update the index of the smallest element
                min_index = j
        # Swap the smallest element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Test the sorting functions
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
print("Sorted array (bubble sort):", bubble_sort(arr.copy()))
print("Sorted array (selection sort):", selection_sort(arr.copy()))