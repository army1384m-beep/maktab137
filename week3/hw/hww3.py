print("bubble_sort".center(50, '-'))
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [5, 1, 4, 2]
result = bubble_sort(numbers)
print("outcome: ", result)



# print("quick_sort".center(50, '-'))
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[-1] 
#     left = []
#     right = []
    
#     for x in arr[:-1]:
#         if x <= pivot:
#             left.append(x)
#         else:
#             right.append(x)
    
#     return quick_sort(left) + [pivot] + quick_sort(right)

# numbers = [5, 1, 4, 2]
# result = quick_sort(numbers)
# print(result)