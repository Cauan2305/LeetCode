class Solution(object):
    def twoSum(self, nums:list, target:int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            for reverseIndex in range(len(nums)-1,-1,-1):
                if index!= reverseIndex and  (nums[index] +nums[reverseIndex]) == target:
                    return [index,reverseIndex]
        
        
nums=[3,3]

target=6

print(Solution().twoSum(nums,target))
