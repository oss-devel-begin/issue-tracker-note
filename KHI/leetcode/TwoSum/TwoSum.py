class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i

        print ("dict = " + len(dict))
        for i in range(0, len(dict)-1):
            print("dict[" + "nums[ " + i + "] + " + "dict[" + "nums[ " + i+1 + "]")
            if(dict.get(nums[i]) + dict.get(nums[i+1])== target):
                return i, i+1

