class Solution(object):
    def twoSum(self, nums, target):
        dics = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dics:
                return [dics[diff], i]
            dics[nums[i]] = i 