class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        """
        Since I solved 533 (Reshaping matrix) first before doing this
        I am going to solve this borrowing some stuff from 533

        Step 1 is checking if it's possible or not, if not, return empty array
        row*column (m and n) always should be the same as the values in the 1D array
        After than, we start a loop with m (row):
        In every loop (row), we thrown in n (column) numbers of value

        Login for the array slice is start value is row * column (current start value)
        End value is row * column + column (start value + how many values to put as column)
        """

        new_array = []

        if (m*n != len(original)):
            return []
        else:
            for row in range(m):
                new_array.append(original[row*n : row*n+n])

        return new_array
