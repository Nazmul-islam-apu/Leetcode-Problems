class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        #Brute Force

        l = len(nums)
        for i in range(l-1):
            for j in range(i+1,l):
                if(nums[i]+nums[j]==target):
                    return (i,j)
        """

        # Hash Table
        final = dict()
        l = len(nums)
        for i in range(l):
            dif = target - nums[i]
            if (nums[i] in final):
                return (i, final[nums[i]])
            else:
                final[dif] = i
