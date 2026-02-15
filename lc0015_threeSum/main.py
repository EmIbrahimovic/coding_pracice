from collections import defaultdict
from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        nums_lookup = defaultdict(list[int])
        for i, num in enumerate(nums):
            nums_lookup[num].append(i)
        
        all_triples = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                target = - nums[i] - nums[j]
                if target not in nums_lookup:
                    continue
                
                idx_list = nums_lookup[target]
                k = idx_list[len(idx_list) - 1]
                if k > j:
                    all_triples.add((nums[i], nums[j], nums[k]))

        
        return [[ai, aj, ak] for ai, aj, ak in all_triples]
        