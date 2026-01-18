def insertion_sort(lst):
    n = len(lst)
    for current in range (1,n):
        currentcard = lst[current]
        correctpossition = current - 1
        
        while correctpossition >= 0:
            if currentcard > lst[correctpossition]:
                break
            else:
                lst[correctpossition+1] = lst[correctpossition]
                correctpossition -= 1
            lst[correctpossition + 1] = currentcard
    return lst
lst = [12, 11, 13, 5, 6]
print(insertion_sort(lst))