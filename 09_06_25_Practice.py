# 75. Sort Colors
from operator import index

# nums = [2,0,2,1,1,0]
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

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#
#     less = [x for x in arr[1:] if x <= pivot]
#     greater = [x for x in arr[1:] if x > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)



# As we know that there are only three numbers so we can use elif statements to create a Flow

# first = 0
# last = len(nums) - 1
# index = 0
#
# while index <= last:
#     if nums[index] == 0:
#         nums[first], nums[index] = nums[index], nums[first]
#         first += 1
#         index += 1
#     elif nums[index] == 2:
#         nums[last], nums[index] = nums[index], nums[last]
#         last -= 1
#     else:
#         index += 1
#
# print(nums)

























# 16. 3Sum Closest

nums = [-1,2,1,-4]
target = 1
min_diff = float('inf')

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):

            total = nums[i] + nums[j] + nums[k]
            diff = abs(total - target)

            if diff < min_diff:
                min_diff = diff
                closest_sum = total


print(closest_sum)

