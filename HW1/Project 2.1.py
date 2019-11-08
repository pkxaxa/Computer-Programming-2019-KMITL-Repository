TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0
Gross_Income = float(input("Enter the gross income: "))
Num_Dependents = float(input("Enter the number of dependents: "))
Net_Income = (Gross_Income - STANDARD_DEDUCTION) - (DEPENDENT_DEDUCTION *
Num_Dependents)
Income_Tax = Net_Income * TAX_RATE
print ("The income tax is ฿{:0.2f}".format(Income_Tax))
