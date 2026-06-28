class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seq = 1
        longest = 1
        num_set = set(nums)
        i = 0
        cp = nums.copy()

        while i < len(nums):
            if cp[i] - 1 in num_set:
                seq += 1
                cp[i] -= 1
            else:
                if longest < seq:
                    longest = seq
                seq = 1
                cp = nums.copy()
                i += 1
        
        return longest
