def sort012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr

# Example usage:
arr1 = [0, 1, 2, 0, 1, 2]
arr2 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

print(sort012(arr1))  # Output: [0, 0, 1, 1, 2, 2]
print(sort012(arr2))  # Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
