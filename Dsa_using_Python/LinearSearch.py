import time
import numpy as np
start = time.time()
def search(ls,x):
    for i in range(len(ls)):
        if ls[i]==x:
            return i

n = int(input("Enter number of elements:"))
a = list(map(int,input("Enter the elements:").strip().split()))[:n]
key = int(input("Enter the element to search:"))
print("Your element is present at index",search(a,key))
end = time.time()
ti = end-start
print("Time taken to search:",ti)
