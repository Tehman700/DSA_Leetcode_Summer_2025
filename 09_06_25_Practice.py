# 75. Sort Colors

nums = [2,0,2,1,1,0]
# as we know that 0 red
# 1 for white
# 2 for Blue

# Simple Bubble sort implementation
# for i in range(len(nums)):
#     swapped = False
#     for j in range(0,len(nums) - i  -1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
#             swapped = True
#
#     if swapped == False:
#         break



# Lets use more efficient algorithm
# Using Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]

    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)



sorted_arr = quick_sort(nums)
print(sorted_arr)