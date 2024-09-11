def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Splitting array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the arrays
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted arrays
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements of left (if any)
    result.extend(left[i:])
    # Add remaining elements of right (if any)
    result.extend(right[j:])

    return result

a = [20, 12, 34, 10, 52, 19]
print("The sorted array using merge sort:", merge_sort(a))
