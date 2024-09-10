def find_missing_number(arr):
    n = len(arr) + 1  # Since arr is of size n-1
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    arr_sum = sum(arr)  # Sum of elements in the array
    missing_number = total_sum - arr_sum  # The missing number
    return missing_number

# Test Case 1
arr1 = [1, 2, 4, 5]
print("Test Case 1 - Input: [1, 2, 4, 5] -> Missing number:", find_missing_number(arr1))  # Expected output: 3

# Test Case 2
arr2 = [2, 3, 4, 5]
print("Test Case 2 - Input: [2, 3, 4, 5] -> Missing number:", find_missing_number(arr2))  # Expected output: 1

# Test Case 3
arr3 = [1, 2, 3, 4]
print("Test Case 3 - Input: [1, 2, 3, 4] -> Missing number:", find_missing_number(arr3))  # Expected output: 5

# Test Case 4
arr4 = [1]
print("Test Case 4 - Input: [1] -> Missing number:", find_missing_number(arr4))  # Expected output: 2

# Test Case 5 (Large input)
arr5 = list(range(1, 1000000))  # Array from 1 to 999999
print("Test Case 5 - Input: [1, 2, 3, ..., 999999] -> Missing number:", find_missing_number(arr5))  # Expected output: 1000000

# Edge Case 1: Smallest possible array, n = 2
arr_edge1 = [2]
print("Edge Case 1 - Input: [2] -> Missing number:", find_missing_number(arr_edge1))  # Expected output: 1

# Edge Case 2: Largest possible array, n = 10^6
arr_edge2 = list(range(1, 1000000))  # Same as Test Case 5
print("Edge Case 2 - Input: [1, 2, 3, ..., 999999] -> Missing number:", find_missing_number(arr_edge2))  # Expected output: 1000000
