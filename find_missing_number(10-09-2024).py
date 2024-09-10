def find_missing_number(arr):
    n = len(arr) + 1  
    total_sum = n * (n + 1) // 2  
    arr_sum = sum(arr)  
    missing_number = total_sum - arr_sum  
    return missing_number

# Test Case 1
arr1 = [1, 2, 4, 5]
print("Test Case 1 - Input: [1, 2, 4, 5] -> Missing number:", find_missing_number(arr1))  

# Test Case 2
arr2 = [2, 3, 4, 5]
print("Test Case 2 - Input: [2, 3, 4, 5] -> Missing number:", find_missing_number(arr2)) 

# Test Case 3
arr3 = [1, 2, 3, 4]
print("Test Case 3 - Input: [1, 2, 3, 4] -> Missing number:", find_missing_number(arr3))  

# Test Case 4
arr4 = [1]
print("Test Case 4 - Input: [1] -> Missing number:", find_missing_number(arr4))  

# Test Case 5 (Large input)
arr5 = list(range(1, 1000000))  
print("Test Case 5 - Input: [1, 2, 3, ..., 999999] -> Missing number:", find_missing_number(arr5))  

# Edge Case 1: Smallest possible array, n = 2
arr_edge1 = [2]
print("Edge Case 1 - Input: [2] -> Missing number:", find_missing_number(arr_edge1))  

# Edge Case 2: Largest possible array, n = 10^6
arr_edge2 = list(range(1, 1000000))  
print("Edge Case 2 - Input: [1, 2, 3, ..., 999999] -> Missing number:", find_missing_number(arr_edge2)) 
