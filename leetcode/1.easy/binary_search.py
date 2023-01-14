class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if target > nums[mid]:
                # search the later half
                start = mid + 1
            elif target < nums[mid]:
                # search the first half
                end = mid - 1
            else:
                return mid

        return -1
