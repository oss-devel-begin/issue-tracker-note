class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i+1,len(nums)):
                b = nums[j]
                if (a+b == target):
                    return i, j          