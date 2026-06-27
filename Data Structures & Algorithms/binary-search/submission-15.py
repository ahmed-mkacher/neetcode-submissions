class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            pos = (i + j) // 2
            mid = nums[pos]

            if mid == target:
                return pos

            if mid > target:
                j = pos - 1
                
            if mid < target:
                i = pos + 1

        return -1
