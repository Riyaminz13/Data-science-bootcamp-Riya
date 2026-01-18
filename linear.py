def linear_search(arr, target):
    size = len(arr)
    for index in range (0,size):
        if arr[index] == target:
            return index
    return -1
ar = [20,75,33,70,2]
tra = 33
print(linear_search(ar, tra))