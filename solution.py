class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i in range(len(nums)):
            if target - nums[i] in check:
                return[i,check[target - nums[i]]]
            else:
                check[nums[i]] = i