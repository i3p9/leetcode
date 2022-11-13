class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        """
        the idea is to loop through the tax brackets, calculating tax
        and removing that specific amount of income from the total income variable

        First we check if the tax bracket amount minus previous amount
        (which results in the actual amount for calculating that brackets tax)

        if it's less than income, then the previously calculated brackets tax amount needs to be paid, and then substract that amount from our income

        if it's MORE than income OR same, that means we have reached the end of calculation, so we take just the income and calculate tax on it, since the income is well below the bracket.

        the last elif can be condensed to a basic else, but keeping it like that
        so future me understands it correctly
        """
        prev = 0
        tax = 0.00
        if income == 0:
            return 0.00


        for i in range(len(brackets)):
            if income <= 0:
                break
            if brackets[i][0]-prev < income:
                income_to_tax = brackets[i][0] - prev
                tax = ((income_to_tax*brackets[i][1])/100) + tax
                income = income - income_to_tax
                prev = brackets[i][0]
            elif brackets[i][0]-prev >= income:
                tax = ((income*brackets[i][1])/100) + tax
                income = 0

        return tax
