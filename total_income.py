"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main(total_months=None):
    """Display income report for incomes over a given number of months."""
    incomes = []
    total_months = int(input("How many months? "))

    for month in range(1, total_months + 1):
        income = float(input("Enter income for month " + str(total_months) + ": "))
        incomes.append(income)
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, total_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()