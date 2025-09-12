# Ask the user to enter their first name, middle initial and
# last name.  Concatenate them together with spaces in between
# and print out the result.

First = input("Please enter your first name: ")
MiddleInitial = input("Please enter your middle initial: ")
Last = input("Please enter your last name: ")
Income = input("Please enter your annual income: ")
MonthlyIncome = float(Income) / 12
FullName = First + " " + MiddleInitial + " " + Last

# Now print in different variants
print("Your full name is", FullName)
print(f"Your full name is {First} {MiddleInitial} {Last}")
print("Your full name is %s %s %s" % (First, MiddleInitial, Last))
print("Your full name is {} {} {}".format(First, MiddleInitial, Last))
print("Your full name is {2} {0} {1}".format(First, MiddleInitial, Last))
print("Your full name is " + " ".join([First, MiddleInitial, Last]))
print(f"Your monthly income is {MonthlyIncome:.2f}")
print("Your monthly income is %.2f" % MonthlyIncome)
