import time
start = time.time()
def InsertionSort(a):
    for i in range(1,len(a)):
        temp = a[i]
        j = i-1
        while j>=0 and temp<a[j]:
            a[j+1] = a[j]
            j-=1
        a[j+1]=temp

a = [10,5,13,8,2]
print("Before Sorting:")
print(a)
InsertionSort(a)
print("After Sorting:")
print(a)
end = time.time()
print("Time taken to search",end-start,"seconds")

        
