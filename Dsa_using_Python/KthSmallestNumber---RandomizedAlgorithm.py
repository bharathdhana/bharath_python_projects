import random

def kthSmallest(arr, l, r, k):
    if k > 0 and k <= r - l + 1:
        pos = randomPartition(arr, l, r)
        
        if pos - l == k - 1:
            return arr[pos]

        if pos - l > k - 1:
            return kthSmallest(arr, l, pos - 1, k)

        return kthSmallest(arr, pos + 1, r, k - pos + l - 1)

    return float('inf')

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            swap(arr, i, j)
            i += 1
    swap(arr, i, r)
    return i

def randomPartition(arr, l, r):
    n = r - l + 1
    pivot = random.randint(0, n - 1)
    swap(arr, l + pivot, r)
    return partition(arr, l, r)

# Code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("Kth smallest element is", kthSmallest(arr, 0, n - 1, k))
