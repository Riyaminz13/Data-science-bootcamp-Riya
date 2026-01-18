def selction_sort(lst):
    n = len(lst)
    for passes in range (0,n-1):
        min_value = passes
        for i in range (passes+1,n):
            if lst[i]<lst[min_value]:
                lst[i],lst[min_value] = lst[min_value],lst[i]
    return lst
lst = [64, 25, 12, 22, 11]
print(selction_sort(lst))