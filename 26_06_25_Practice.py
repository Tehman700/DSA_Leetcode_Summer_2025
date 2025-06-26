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














