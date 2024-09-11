import time
start = time.time()
def BinarySearch(arr,k,low,high):
    if high >= low:
        mid = low + (high-low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return BinarySearch(arr,k,low,mid-1)
        else:
            return BinarySearch(arr,k,mid+1,high)
    else:
        return -1

arr = [1,3,5,7,9]
print(arr)
k = int(input("Enter the element at array:"))
result = BinarySearch(arr,k,0,len(arr)-1)
if result != -1:
    print("Element is present at index"+str(result))
else:
    print("Not Found")


BinarySearch(arr,k,0,len(arr)-1)
end = time.time()
print("Time taken to search:",end-start,"seconds")
