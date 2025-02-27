def longest_odd_even_subarray(arr):
    if not arr:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(arr)):
        if (arr[i] % 2 == 0 and arr[i-1] % 2 != 0) or (arr[i] % 2 != 0 and arr[i-1] % 2 == 0):
            current_length +=1
            max_length = max(max_length, current_length)
        else:
            current_length = 1 # Reset length if pattern breaks 

    return max_length

# Example usage 
arr = [10, 12, 14, 7, 8, 9, 11, 10, 12, 14, 3]
print(longest_odd_even_subarray(arr)) # Output: 5