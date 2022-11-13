class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        what if we start from the last index of nums1
        and add two pointers to the two array that points to last index
        third pointer is for where we'll write,
        which starts from last index as well m+n -1 OR len(nums1) - 1
        compare between two pointers

        rough idea ->
        while nums2 pointer is more than 0:
        if nums1_pointer not less than 0 num1 pointer > nums2 pointer ->
        nums1 pointers value gets put there to nums1[write pointer] AND nums1 pointer --
        ---
        else if nums1 pointer < nums2 pointer ->
        num2 pointer value gets put there to nums1[write pointer] AND nums2 pointer --
        lastly write_pointer -- every loop

        *assuming
        nums1 -> s1
        nums2 -> s2
        """

        s1 = m - 1
        s2 = n - 1
        write_pointer = m + n - 1

        while s2 >= 0:
            if s1 >= 0 and nums1[s1] > nums2[s2]:
                nums1[write_pointer] = nums1[s1]
                s1 -= 1
            else:
                nums1[write_pointer] = nums2[s2]
                s2 -= 1

            write_pointer -= 1

