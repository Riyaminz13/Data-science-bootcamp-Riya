def bubble_sort(lst):
    n = len(lst)
    for passes in range (n):
        for j in range (0, n-1-passes):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    return lst
lst = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(lst))