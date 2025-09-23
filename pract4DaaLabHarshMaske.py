import sys

def print_subarray(arr, start, end):
    print("{ ", end="")
    for i in range(start, end + 1):
        print(arr[i], end=" ")
    print("}", end="")

def max_of_three(a, b, c):
    return max(max(a, b), c)

def max_crossing_sum(arr, low, mid, high):
    sum_val = 0
    left_sum = -sys.maxsize
    for i in range(mid, low - 1, -1):
        sum_val += arr[i]
        if sum_val > left_sum:
            left_sum = sum_val
    sum_val = 0
    right_sum = -sys.maxsize
    for i in range(mid + 1, high + 1):
        sum_val += arr[i]
        if sum_val > right_sum:
            right_sum = sum_val
    return max_of_three(left_sum + right_sum, left_sum, right_sum)

def max_sum_recursive(arr, low, high):
    if low == high:
        print(f"Individual element found: {arr[low]}")
        return arr[low]
    mid = low + (high - low) // 2
    print("\n--- Dividing array segment ", end="")
    print_subarray(arr, low, high)
    print(" ---")
    print("First subarray: ", end="")
    print_subarray(arr, low, mid)
    print("\nSecond subarray: ", end="")
    print_subarray(arr, mid + 1, high)
    print()
    left_max_sum = max_sum_recursive(arr, low, mid)
    right_max_sum = max_sum_recursive(arr, mid + 1, high)
    cross_max_sum = max_crossing_sum(arr, low, mid, high)
    print("\n--- Applying Concept for segment ", end="")
    print_subarray(arr, low, high)
    print(" ---")
    print(f"Max sum in left half: {left_max_sum}")
    print(f"Max sum in right half: {right_max_sum}")
    print(f"Max sum for crossing subarray: {cross_max_sum}")
    result = max_of_three(left_max_sum, right_max_sum, cross_max_sum)
    print(f"=> Maximum of ({left_max_sum}, {right_max_sum}, {cross_max_sum}) is {result}")
    return result

if __name__ == "__main__":
    originalArray = [1, 2, 3, 4, 5, 6, 7]
    # originalArray = [-2, -5, 6, -2, -3, 1, 5, -6]
    size = len(originalArray)
    print("Applying Maximum Sum Subarray using Divide and Conquer:")
    print("Original Array: ", end="")
    print_subarray(originalArray, 0, size - 1)
    print()
    maxSum = max_sum_recursive(originalArray, 0, size - 1)
    print("\n------------------------------------------------")
    print(f"Final Maximum Sum of a Contiguous Subarray is: {maxSum}")
    print("------------------------------------------------")
