class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        count = {}
        majority_bound = len(nums) // 2 + 1
        for i in nums:        
            if i in count:
                count[i] += 1
                if count[i] >= majority_bound:
                    return i
            else:
                count[i] = 1