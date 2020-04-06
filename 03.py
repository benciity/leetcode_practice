class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre=nums[0]
        for index in range(1,len(nums)):
            if pre==nums[index]:
                return pre
            pre=nums[index]
