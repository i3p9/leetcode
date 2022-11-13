class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorithm
        local_max = 0
        global_max = -inf
        start = 0
        end = 0
        s = 0
        '''
        This is unrelated to specific problem but will be needed if
        we are told to print the sub-array itself
        '''
        
        for i in range(len(nums)):
            if (nums[i] <= local_max + nums[i]):
                local_max = local_max + nums[i]
            else:
                local_max = nums[i]
                s = i
            if (local_max > global_max):
                global_max = local_max
                start = s
                end = i
                
        '''
        So now start and end has the index of the subarray
        '''
        return global_max
                
        
