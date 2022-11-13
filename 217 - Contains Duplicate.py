class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        using set, elaborately
        Since set only stores one instance of something, we can quickly
        check the uniqueness of the array
        '''
        uniqueSet = set()
        for val in nums:
            if val in uniqueSet:
                return True
            else:
                uniqueSet.add(val)
        return False
