class Solution(object):
    def twoSum(self, nums, target):
    
        
        for i in range (len(nums)):
            for j in range (i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []    
                 
        
    
        class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return zero
        i = 0
        for j in range(1, (len(nums))):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return  i + 1         