class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """
        Going to do this in two steps
        Step 1 -> Convert (Flatten) the 2D Array into a 1D array using O(m+n)
        Step 2a -> Check if r*c is equal to 1D array's length,
        if not, return original matrix
        Step 2a -> If equal, start a loop of r (row) loops

        When in a row, put the number of c (columns) values in the new 2D array

        Logic => new_array.append(flat_array[row*c : row*c+c])

        Here: row*c is the start value of the 1D Array, row*c + c is the end value.
        (+c) basically denotes how many columns we want in the 2D Array
        """

        flat_array = []

        #converting to 1D array
        for row in mat:
            for col in row:
                flat_array.append(col)

        new_matrix = []
        #checking for the rule of the reshape op being possible and legal
        if (r*c != len(flat_array)):
            return mat #returning the original matrix if we cant reshape it
        else:
            for row in range(r):
                new_matrix.append(flat_array[row*c : row*c+c]) #reshaping

        return new_matrix
