class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        had to google a bit to find out how to get any element in pascal's triangle
        which is nCr problem (n is now, r is column)
        So for rowIndex 3, it will be
        [3C0,3C1,3C2,3C3]...
        Easy way is (submitted at 11/14/2022 01:50, 93%, 66%)
        for i in range(rowIndex+1): ans.append(math.comb(rowIndex,i))
        To get the bionomial coefficients manually:
        eg 4C0 - > 1
        to 4C1 -> 4 / 1
        to 4C2 -> 4*3 / 1*2
        to 4C3 -> 4*3*2 / 1*2*3
        Or 4C4 -> 4*3*2*1 / 1*2*3*4
        so numerator/Denominator will be rowIndex * num/denom
        and each loop the numerator will decrease
        and denominator will increase
        """
        ans = [1]
        if rowIndex == 0:
            return ans
        num = rowIndex
        denom = 1
        for i in range(1,rowIndex+1):
            ans.append(int(ans[-1]* num/denom))
            num -= 1
            denom += 1

        return ans

        '''
        """slowest one"""
        triangle = []

        for row in range(1,rowIndex+2):
            cols = []
            for col in range(row):
                if col == 0 or col == (row-1):
                    cols.append(1)
                else:
                    cols.append(triangle[-1][col-1] + triangle[-1][col])
            triangle.append(cols)

        return triangle[rowIndex]

        """Easiest/fastest One (using math.comb)"""
        ans = []
        for i in range(rowIndex+1):
            ans.append(math.comb(rowIndex,i))
        return ans


        '''
