## linear search

# def linear_search(arr,target):
#     size=len(arr)
#     for index in range(0,size):
#         if (arr[index]==target):
#             return index
#     return -1

# my_list=[10,40,70,100,30]
# target = 70
# # target=input("enter the target: ")
# result=linear_search(my_list,target)

# print(result)

## binary search 

# def binary_seach(arr,target):
#     size=len(arr)

#     start=0
#     end = size -1

#     while(start <= end):
#         mid = (start + end)//2

#         if(arr[mid]==target):
#             return mid 
#         elif(arr[mid]>target):
#             end = mid -1 
#         elif(arr[mid]<target):
#             start = mid + 1
#     return -1

# sorted_list = [10,23,35,45,50,70,85]
# target=50

# result= binary_seach(sorted_list,target)
# print(result)

## bubble short

def bubble_short (arr):
    n = len(arr)
    for passes in range(0,n-1):

        for j in range (0,n-1):
            if (arr[j]>arr[j+1]):
             arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr 

unsorted_list = [120, 11,350,40,30,190,70]
sorted_list= bubble_short(unsorted_list)
print ("shorted list : ",sorted_list)