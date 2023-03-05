import random
value_list = list(range(10))
random.shuffle(value_list)
print(value_list)

def selection_sort(arr):
    for idx, i in enumerate(arr):
        min_idx = idx
        for jdx in range(idx+1, len(arr)):
            if arr[jdx] < arr[min_idx]:
                min_idx = jdx
        tmp = arr[idx]
        arr[idx] = arr[min_idx]
        arr[min_idx] = tmp
    return arr

def bubble_sort(arr):
    for idx in range(len(arr)):
        for jdx in range(0, len(arr)-1-idx):
            print(jdx, 2)
            if arr[jdx] > arr[jdx+1]:
                tmp = arr[jdx]
                arr[jdx] = arr[jdx+1]
                arr[jdx+1] = tmp
    return arr

def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i] < arr[i-1]:
                tmp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = tmp
    return arr

result = insertion_sort(value_list)
print(result)
