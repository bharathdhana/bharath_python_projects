def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[-1]
    less = []
    greater = []
    equal = []
    for element in arr:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equal.append(element)
            
        sorted_less = quick_sort(less)
    sorted_greater = quick_sort(greater)
    return sorted_less + equal + sorted_greater

a = [20,12,34,10,52,19]
print("The sorted array using quick sort:",quick_sort(a))
    
    
