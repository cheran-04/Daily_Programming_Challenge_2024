def dutch_national_flag(arr):
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr

user_input = input("Enter a list of numbers (0s, 1s, and 2s) separated by spaces: ")
arr = list(map(int, user_input.split()))

sorted_arr = dutch_national_flag(arr)

print("Sorted array:", sorted_arr)
