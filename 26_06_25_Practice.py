# 33. Search in Rotated Sorted Array


# nums = [4,5,6,7,0,1,2]
# # First Sort this array to find the where 4rth was
# target_number = nums[0]
# final_target_number = 0
# nums.sort()
# print(nums)
# k = nums.index(target_number)
# print(k)
#
#
# new_list = []
#
# # Now applying Logic of if_else
# if final_target_number == nums[k]:
#     print("TRUE")
# elif final_target_number < nums[k]:
#     new_list = nums[:k]
# elif final_target_number > nums[k]:
#     new_list = nums[k+1:]
#
#
# left, right = 0, len(new_list) -1
# while left <= right:
#     mid = (left + right) // 2
#
#     if new_list[mid] == final_target_number:
#         print("True")
#         break
#     elif new_list[mid] < final_target_number:
#         left = mid + 1
#     else:
#         right = mid - 1
#
# print("-1")













## 81. Search in Rotated Sorted Array II

# Exact Same as Above





# 153. Find the Minimum in Rotated Sorted Array

# nums = [3,4,5,1,2]
#
# working = sorted(nums)
#
# rotated_times = 0
# print(nums)
# print(working)
# if nums == working:
#     rotated_times = len(nums)
# else:
#     k = nums.index(working[0])
#     rotated_times = len(nums[:k])
#
#
# print(rotated_times)

















# 2555. Maximize Win from Two Segments

prize_positions = [1,2,3,4]
k = 0



if k == 0:
    print(min(2, len(set(prize_positions))))
    exit()  # Exit early

unique = list(set(prize_positions))
print(prize_positions)
print(unique)

final_2D_list = []

for i in range(0,len(unique)):
    starting = unique[i]
    ending = unique[i] + k
    print(starting, ending)

    result = [x for x in prize_positions if starting <= x <= ending]
    final_2D_list.append(result)

max_total = 0
for i in range(len(final_2D_list)):
    for j in range(i, len(final_2D_list)):
        total = len(set(final_2D_list[i]) | set(final_2D_list[j]))
        max_total = max(max_total, total)

print(max_total)
