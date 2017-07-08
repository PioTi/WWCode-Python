""" Aling Nena's Cashier Challenge
Author:
Description: During closing, Aling Nena counts from her vault the day's total income and
also the total amount of all her paper bills.

Help Aling Nena count her total income and total amount of her paper bills
from a list of cash money and using a loop!
"""


def is_coins(money):
    """ Determine if the money is a coin
    :param money: (Integer)
    :return: (Boolean)

    Examples:
        >>>  print(is_coins(20))
        False
        >>>  print(is_coins(1))
        True
    """
  
    if money < 20:
        return True
    return False


cash_on_vault = [1, 5, 100, 10, 50, 50, 20, 5, 1, 1000, 1000, 500, 5, 200]
cash = 0
bills = 0
moneyCheck = False
###for loop for the logic
for row in cash_on_vault:
    cash+=row
    moneyCheck = is_coins(row)
   # print('moneyCheck :',moneyCheck)
    if(moneyCheck == False):
        bills+=row

print("Hi Aling Nena! Your total income for the day is :",cash)
print("The total amount of your paper bills is :",bills)
