def binary_search (arr,target):
    size = len(arr)

    start = 0
    end = size - 1
    while(start <= end):
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid -1
        elif target > arr[mid]:
            start = mid +1
    return -1
shorted_arr = [10,33,45,66,78,90,100]
target = 900
print(binary_search(shorted_arr,target))