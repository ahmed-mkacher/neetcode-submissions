class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
             
        seq = 1
        seqs = []
        i = 0
        cp = nums.copy()

        while i < len(nums):
            if cp[i] - 1 in nums:
                seq += 1
                cp[i] -= 1
            else:
                seqs.append(seq)
                seq = 1
                cp = nums.copy()
                i += 1
        
        return max(seqs)
