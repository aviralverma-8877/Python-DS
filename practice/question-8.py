#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==0:
            return 0
        s = None
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)+1):
                if s == None:
                    s = sum(nums[i:j])
                else:
                    s = max(sum(nums[i:j]),s)
        return s

s= Solution()
print(s.maxSubArray([2,5]))