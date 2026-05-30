# ==================================================
# 1 NameError
# ==================================================

try:

    print(name)

except NameError as e:

    print(e)


# ==================================================
# 2 IndentationError
# ==================================================

# This causes compile-time error
# Cannot be handled using try-except

# if True:
# print("Hello")


# ==================================================
# 3 IOError
# ==================================================

try:

    file = open("abc.txt","r")

except IOError as e:

    print(e)


# ==================================================
# 4 EOFError
# ==================================================

# Happens mostly in online input situations

try:

    value = input("Enter Value: ")

except EOFError:

    print("EOFError Occurred")


# ==================================================
# 5 ZeroDivisionError
# ==================================================

try:

    print(10/0)

except ZeroDivisionError as e:

    print(e)


# ==================================================
# 6 ValueError
# ==================================================

try:

    num = int("abc")

except ValueError as e:

    print(e)


# ==================================================
# 7 TypeError
# ==================================================

try:

    result = 10 + "20"

except TypeError as e:

    print(e)


# ==================================================
# 8 Divide Numbers Safely
# ==================================================

try:

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = num1 / num2

    print(result)

except ZeroDivisionError:

    print("Cannot Divide By Zero")

except ValueError:

    print("Enter Valid Numbers")


# ==================================================
# 9 Input Validation
# ==================================================

try:

    age = int(input("Enter Age: "))

    print(age)

except ValueError:

    print("Age Must Be Integer")


# ==================================================
# 10 Try Except Else
# ==================================================

try:

    num = int(input("Enter Number: "))

except ValueError:

    print("Invalid Input")

else:

    print("Valid Input")


# ==================================================
# 11 Reciprocal Calculator
# ==================================================

try:

    num = int(input("Enter Number: "))

    result = 1 / num

except ZeroDivisionError:

    print("Reciprocal Not Possible")

else:

    print(result)


# ==================================================
# 12 Multiple Exceptions
# ==================================================

try:

    num = int(input("Enter Number: "))

    print(100 / num)

except ValueError:

    print("Invalid Number")

except ZeroDivisionError:

    print("Cannot Divide By Zero")


# ==================================================
# 13 Multiple Exceptions In One Line
# ==================================================

try:

    num = int(input("Enter Number: "))

    print(100 / num)

except (ValueError,ZeroDivisionError):

    print("Error Occurred")


# ==================================================
# 14 Finally Block
# ==================================================

try:

    print("Program Running")

except:

    print("Error")

finally:

    print("Always Executes")


# ==================================================
# 15 File Closing Example
# ==================================================

file = None

try:

    file = open("sample.txt","r")

    print(file.read())

except FileNotFoundError:

    print("File Not Found")

finally:

    if file:

        file.close()

    print("File Closed")


# ==================================================
# 16 Raise ValueError Manually
# ==================================================

age = -5

try:

    if age < 0:

        raise ValueError("Age Cannot Be Negative")

except ValueError as e:

    print(e)


# ==================================================
# 17 Raise Exception
# ==================================================

try:

    raise Exception("Custom Error")

except Exception as e:

    print(e)


# ==================================================
# 18 Custom Exception
# ==================================================

class MyError(Exception):

    pass

try:

    raise MyError("My Custom Exception")

except MyError as e:

    print(e)


# ==================================================
# 19 ValueTooSmallError
# ==================================================

class ValueTooSmallError(Exception):

    pass

try:

    num = 5

    if num < 10:

        raise ValueTooSmallError("Value Too Small")

except ValueTooSmallError as e:

    print(e)


# ==================================================
# 20 ValueTooLargeError
# ==================================================

class ValueTooLargeError(Exception):

    pass

try:

    num = 150

    if num > 100:

        raise ValueTooLargeError("Value Too Large")

except ValueTooLargeError as e:

    print(e)


# ==================================================
# 21 Bank Balance Exception
# ==================================================

class InsufficientBalanceError(Exception):

    pass

balance = 5000

withdraw = 7000

try:

    if withdraw > balance:

        raise InsufficientBalanceError(
            "Insufficient Balance"
        )

except InsufficientBalanceError as e:

    print(e)


# ==================================================
# 22 Age Validation Exception
# ==================================================

class InvalidAgeError(Exception):

    pass

try:

    age = -2

    if age < 0:

        raise InvalidAgeError(
            "Age Cannot Be Negative"
        )

except InvalidAgeError as e:

    print(e)


# ==================================================
# 23 Positive Number Assertion
# ==================================================

num = 10

assert num > 0

print("Positive Number")


# ==================================================
# 24 Assertion Error Demo
# ==================================================

try:

    num = -5

    assert num > 0,"Number Must Be Positive"

except AssertionError as e:

    print(e)


# ==================================================
# 25 Square Root Assertion
# ==================================================

import math

num = 25

assert num >= 0,"Negative Number Not Allowed"

print(math.sqrt(num))


# ==================================================
# 26 Password Validation Assertion
# ==================================================

password = "Python123"

try:

    assert len(password) >= 8,\
        "Password Too Short"

    print("Valid Password")

except AssertionError as e:

    print(e)


# ==================================================
# 27 Nested Try Except
# ==================================================

try:

    try:

        num = int(input("Enter Number: "))

        print(100 / num)

    except ZeroDivisionError:

        print("Cannot Divide By Zero")

except ValueError:

    print("Invalid Input")


# ==================================================
# 28 User Defined Calculator
# ==================================================

try:

    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    print("Addition =",a+b)
    print("Division =",a/b)

except ValueError:

    print("Invalid Input")

except ZeroDivisionError:

    print("Cannot Divide By Zero")


# ==================================================
# 29 Voting Eligibility Validation
# ==================================================

try:

    age = int(input("Enter Age: "))

    if age < 18:

        raise ValueError(
            "Not Eligible For Voting"
        )

    print("Eligible")

except ValueError as e:

    print(e)


# ==================================================
# 30 ATM Withdrawal Validation
# ==================================================

balance = 10000

try:

    amount = int(input("Enter Amount: "))

    if amount > balance:

        raise Exception(
            "Insufficient Balance"
        )

    balance -= amount

    print("Remaining Balance =",balance)

except Exception as e:

    print(e)