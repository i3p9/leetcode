from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Basically using python's counter to quickly store how many
        times a value in nums1 array has been seen
        then going through nums2 values and if the
        frequency of the value is more than 0 in nums1_counter
        we put that value in a new array and
        decrease that specific frequency one time

        if the arrays are sorted, maybe a different way
        where we start at index 0 of both array and go though them
        via 2 counters and change the counters by comparing two arrays
        values??? maybe idk
        """

        nums1_counter = Counter(nums1)
        intersected = []

        for val in nums2:
            if nums1_counter[val] > 0:
                intersected.append(val)
                nums1_counter[val] -= 1

        return intersected
