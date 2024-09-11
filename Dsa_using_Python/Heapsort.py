import time
start = time.time()
def heapify(array,a,b):
    largest = b
    l = 2*b+1
    root = 2*b+2
    if l<a and array[b] and array[l]:
        largest = l
    if root<a and array[largest] < array[root]:
        largest = root

    #Change root
    if largest != b:
        array[b],array[largest] = array[largest],array[b]
        heapify(array,a,largest)


#Sort an array of given size
def Heap_Sort(array):
    a = len(array)
    #Max heap..
    for b in range(a//2 -1, -1, -1):
        heapify(array,a,b)

    #Extract elements
    for b in range(a-1,0,-1):
        array[b],array[0] = array[0],array[b]
        heapify(array,b,0)

#Code
array = [7,2,5,6,3,1,8,4]
print("The Original array is:",array)
print(start)
Heap_Sort(array)
a =len(array)
print("Array after sorting:",array)
end = time.time()

def measure_heap_sort_time(array):
    start_time = time.time()
    Heap_Sort(array)
    end_time = time.time()
    return end_time - start_time

print("The required time is:",float(end-start))
    
