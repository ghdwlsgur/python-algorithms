# class Solution(object):
#     def twoSum(self, numbers, target):
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         if target > 0:
#             cp_numbers = [x for x in numbers if x <= target]
#         if target < 0:
#             cp_numbers = [x for x in numbers if x >= target]
#         if target == 0:
#             cp_numbers = numbers
#
#         if len(cp_numbers) == 2:
#             return [numbers.index(cp_numbers[0]) + 1, numbers.index(cp_numbers[1]) + 1]
#         else:
#             start = 0
#             end = -1
#             while start < len(cp_numbers) // 2:
#                 for num in cp_numbers[start+1:]:
#                     if cp_numbers[start] + num == target:
#                         if cp_numbers[start] == num:
#                             return [start+1, numbers.index(num)+2]
#                         return [start+1, numbers.index(num)+1]
#
#                 for num in cp_numbers[:end]:
#                     if cp_numbers[end] + num == target:
#                         return [numbers.index(num)+1, len(cp_numbers)+end+1]
#
#                 start += 1
#                 end -= 1

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target > 0:
            cp_numbers = [x for x in numbers if x <= target]
        if target < 0:
            cp_numbers = [x for x in numbers if x >= target]
        if target == 0:
            cp_numbers = numbers

        if len(cp_numbers) == 2:
            return [numbers.index(cp_numbers[0]) + 1, numbers.index(cp_numbers[1]) + 1]
        else:
            start = 0
            end = len(numbers)- 1
            while start < end:
                curr_sum = numbers[start] + numbers[end]
                if curr_sum == target:
                    return [start + 1, end + 1]
                elif curr_sum < target:
                    start += 1
                else:
                    end -= 1


s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([2, 3, 4], 6))
print(s.twoSum([-1, 0], -1))
print(s.twoSum([0, 0, 3, 4], 0))
print(s.twoSum([-3, 3, 4, 90], 0))
print(s.twoSum([-1, -1, 1, 1, 1, 1, 1, 1, 1, 1], -2))