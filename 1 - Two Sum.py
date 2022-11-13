class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''
        O(n^2) solution

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

        one pass O(n) solution below
        '''

        solve_dict = {}

        for index, value in enumerate(nums):
            if (target - value) in solve_dict:
                return [solve_dict[target-value], index]
            else:
                solve_dict[value] = index
