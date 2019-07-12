# Buggy Python

## Description
This repository contains several buggy python scripts. The purpose of the introduction of bugs is to test your attention to detail and problem solving skills.

## Requirements
The requirements for this project are simple and are as follows:
- Python3

## Instructions
Do not modify the existing logic, just find the bug in the code snippets and correct it.
The expected output when running the script is displayed in `main.py`
Do not modify the `main.py` file.


### Changes Documentation by module and function.

#### File foobar.py foo().

1. Default parameters cannot be mutable values change empty to a null value.
switch from `bar=[]` to `bar=None`.    

#### File IO.py, calculate_unpaid_loans.

1. Fixed Typo on the return statement sun instead of sum function `line 20`. 
2. Fixed Wrong construct of a List comprehension using curly brackets instead of square brackets.
3. Access dictionary correctly fix, from `loan.amount`, `loan.status` to `loan["amount"] ` and `loan["status"]`.
4. Fix to unpaid loan check on line 18, from `!== ` to `==`, to ensure its checking unpaid loans.
5. line 15 Wrong way to access dictionary value, `loans = data("loans")` fix to `loans = data["loans"]`.


#### File IO.py calculate_paid_loans.
1. Access dictionary correctly fix, from `loan.amount`, `loan.status` to `loan["amount"] ` and `loan["status"]`.
2. Fix loan status check on line 27, from identity check `is` to equality check `==`, to ensure its checking paid loans.
3. Fix typo on the return statement sun instead of sum line `29`.
4. line 24 Wrong way to access dictionary value, `loans = data("loans")` fix to `loans = data["loans"]`.


#### File IO.py average_paid_loans.
1. On line `38. sum_paid_loans = sun(paid_loans)` typo when calling the sum function.
2. On line `39` wrong function call `length` instead of len to check list size.
3. line 33 Wrong way to access dictionary value, `loans = data("loans")` fix to `loans = data["loans"]`.


#### File loop.py lambda_array.
1. Wrong initializing of array should be `lambda_methods=list()`
2. Line 11 wrong use of for loop since integer literal (10) is not a iterable, switched to use range function to fix.
3. Line 13 wrong variable name `lambdamethods` switch to `lambda_methods`.
4. Line 13 python list uses append function to add objects to a list and does not have a push function.
