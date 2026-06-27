class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = dict()
        result = []
        for num in nums:
            if num not in elements.keys():
                elements[num] = nums.count(num)
        while k > 0:
            maximum = max(elements.values())
            for num in elements:
                if elements[num] == maximum:
                    result.append(num)
                    k -= 1
                    del elements[num]
                    break
        return result