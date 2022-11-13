class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        The idea is two-fold,
        loop though the number of rows, where rows = cols
        Firstly the constant, >1< in every rows first and last column
        Secondly, for the rest of the columns:
        Summation of previous arrays col value, and col-1 value, as per the equation
        """
        triangle = []
        for row in range(1,numRows+1):
            cols = []
            for col in range(row):
                if (col == 0 or col == (row-1)):
                    #putting 1s in the first and last col of a row
                    cols.append(1)
                else:
                    cols.append(triangle[-1][col-1] + triangle[-1][col])
                    # sum of prev arrays -> cols and prev cols based on current cols
            triangle.append(cols)

        return triangle
