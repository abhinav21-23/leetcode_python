class Solution(object):
    def twoSum(self, nums, target):
        ls = len(nums)
        for i in range(ls):
            for j in range(i + 1, ls):
                if nums[i] + nums[j] == target:
                    return [i, j]
