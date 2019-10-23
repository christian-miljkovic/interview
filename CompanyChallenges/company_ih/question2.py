"""
Problem: Given an amount paid and cost of an item determine the difference in the amount
of bills paid in demnominations starting from $10, $5, $1, 25cents, 10cents, 1cent

input: paid, cost
paid = float 10.50 
cost = float 12.50

output:
2 * 1

output: nums of bill denominations
- $10, $5, $1, 25cents, 10cents, 5cents, 1cents
- 1*10,(keep it empty),1*5, 2*25cents

2.25 / 10 = 0 
2.25 / 5 = 0

if division is greater than 1 then check the mod

2.25 / 1 = 2 and 2.25 % 1 = .25
    - if above is not 0 then
        - .30/25 = 1 and .30%25 = .05
2.25
"""


def differencePaid(amountPaid, costOfProduct):

    denomTen = 0
    denomFive = 0
    denomOne = 0
    denomTwentyFiveCents = 0
    denomTenCents = 0
    denomFiveCents = 0
    denomOneCent = 0

    difference = amountPaid - costOfProduct

    arr = [10, 5, 1, .25, .10 , .1]
    for i in range(0,len(arr)):
        if(10):
            divideAndModulo(difference, arr[10])


def divideAndModulo(diff, value)
    



