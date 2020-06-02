# Calculate the average of numbers given
# --------------------------------------

numbers = int(input("Please enter the amount of items to be included in the list : "))

lst1 = []

for x in range(0, numbers):
    item = int(input("Please enter an item : "))
    lst1.append(item)

average = sum(lst1) / numbers

print("the average of the items in the given list is : ", round(average, 2))

# Determine the sum of all the digits in a given number
# -----------------------------------------------------

number = int(input("Please enter a number : "))

totalSum = 0

while number > 0:
    digit = number % 10
    totalSum = totalSum + digit
    number = number // 10

print("The total sum of all digits in the number is : ", totalSum)

# Reverse a given number
# ----------------------

number2 = int(input("Please enter your number : "))

revNumber = 0

while number2 > 0:
    digit = number2 % 10
    revNumber = revNumber * 10 + digit
    number2 = number2 // 10

print("The reverse of the given number is : ", revNumber)

# OR

number3 = int(input("Please enter your number : "))

lst2 = []

for n in str(number3):
    lst2.append(n)

lst3 = lst2[::-1]

strNumber1 = ''
revNumber2 = 0

for m in lst3:
    strNumber1 = strNumber1 + m

revNumber2 = int(strNumber1)
print("The reverse of the given number is : ", revNumber2)

# Determine the Grade for a student from the given amount of subjects
# -------------------------------------------------------------------

amtS = int(input("How many subjects do you have? "))
totPoints = 0

for z in range(1, amtS + 1):
    s1 = int(input("Please enter the marks of subject no " + str(z) + " : "))
    totPoints = totPoints + s1

avgPoints = totPoints / amtS

if avgPoints >= 90:
    print("You have achieved a Grade: A+")
elif (avgPoints >= 80 and avgPoints < 90):
    print("You have achieved a Grade: A")
elif (avgPoints >= 70 and avgPoints < 80):
    print("You have achieved a Grade: B")
elif(avgPoints >= 60 and avgPoints < 70):
    print("You have achieved a Grade: C")
elif(avgPoints >= 50 and avgPoints < 60):
    print("You have achieved a Grade: D")
elif(avgPoints >= 40 and avgPoints < 50):
    print("You have achieved a Grade: E")
else:
    print("You have achieved a Grade: F")

# Exchange the value of 2 given numbers
# -------------------------------------

nbr1 = int(input("Please enter your 1st number : "))
nbr2 = int(input("Please enter your 2nd number : "))
nbr1 = nbr1 + nbr2
nbr2 = nbr1 - nbr2
nbr1 = nbr1 - nbr2
print("nbr1 is : ", nbr1, " nbr2 is : ", nbr2)

# Determine the number of digits in a given number
# ------------------------------------------------

number2 = int(input("Please enter your number : "))

cntr1 = 0

while number2 > 0:
    cntr1 += 1
    number2 = number2 // 10

print("The number of digits in the number are : ", cntr1)

# Print different structures with characters
# ------------------------------------------

u1 = u"\u0001"
u2 = u"\u2454"

number3 = int(input("Please enter the number of rows required : "))

for i in range(number3, 0, -1):
    print((number3 - i) * u1)

print()

c = 1

for i in range(0, number3 + 2):
    if i == 0:
        print((number3 * 2 - 1) * u1)
    else:
        print((number3 - i) * u1 + c * ' ' + (number3 - i) * u1)
        c += 2

c = 1

for i in range(1, number3 + 1):
    print((number3 - i) * ' ' + c * u1 + (number3 - i) * ' ')
    c += 2

number3 = (number3 - (number3 - 1))
number4 = number3 + 26
cntr3 = 5

while (number3 < number4) and (cntr3 > 0):
    if number3 < (number4 // 4):
        print(u1 * 38)
    elif number3 < ((number4 // 5) * 3):
        if number3 == ((number4 // 5) * 2):
            print(u1 * 8 + '   ' + '    STELLIE   ' + '     ' + u1 * 8)
        else:
            print(u1 * 8 + (' ' * 22) + u1 * 8)
    else:
        cntr3 -= 1
        print(u1 * 38)
    number3 += 1

# Creating a box with a cross in it
# ---------------------------------

number5 = int(input("Please enter your number : "))
number6 = number5 - 1

for a in range(0, number5):
    for b in range(0, number5):
        if b == number6:
            number6 -= 1
            print(u1, sep=" ", end=" ")
        elif b == 0:
            print(u1, sep=" ", end=" ")
        elif a == 0:
            print(u1, sep=" ", end=" ")
        elif a == (number5 - 1):
            print(u1, sep=" ", end=" ")
        elif b == (number5 - 1):
            print(u1, sep=" ", end=" ")
        elif a == b:
            print(u1, sep=" ", end=" ")
        else:
            print(".", sep=" ", end=" ")
    print()

# Determine the Prime numbers in a range
# --------------------------------------

number7 = int(input("Please enter your number : "))

range1 = set(range(2, number7 + 1))
lstP = []

while range1:
    primeNumber = min(range1)
    lstP.append(primeNumber)
    range1 -= set(range(primeNumber, number7 + 1, primeNumber))

print("The List with Prime Numbers are : ", lstP)
