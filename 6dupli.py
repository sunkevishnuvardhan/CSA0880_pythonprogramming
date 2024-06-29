def remove_duplicates(arr):
    if not arr:
        return []

    unique_arr = [arr[0]]

    for num in arr[1:]:
       
        if num != unique_arr[-1]:
            unique_arr.append(num)

    return unique_arr

sorted_array = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6]
print("Original array:", sorted_array)
unique_array = remove_duplicates(sorted_array)
print("Array after removing duplicates:", unique_array)
