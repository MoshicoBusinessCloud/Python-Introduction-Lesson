# from re import T
# from statistics import quantiles
# from tkinter.messagebox import NO
# ==Learning [integer] in Python. When using int function you do not use quotations.
# ===================================================================================================================================

# ===================================================================================================================================
# print(1)
# print(2+20)

# price = 15
# quantiles = 10007

# print(price*quantiles)   # --price multply by quantities

# --if you run this code you should ess this:
# Operators-Keywords-Comments-Type conversion/hands-on.py"
# 1
# 22
# 150105
# PS C:\Users\brown\python-introduction>

# ===================================================================================================================================
#      # ==Learning [string] in Python. When using str function you need put you text in quotations inside of the bracket==#     #
# ----------------------------------------------------------------------------------------------------------------------------------
# ===================================================================================================================================
# print("Hello World")
# print("we are in python session")

# print(type("we are in python session"))

# print(type("1223,23567,759960"))

# Operators-Keywords-Comments-Type conversion/hands-on.py"
# Moses
# we are in python session
# <class 'str'>
# <class 'str'>
# PS C:\Users\brown\python-introduction>
# ===================================================================================================================================
# -----------------------------------------------------------------------------------------------------------------------------------
#      # ==Learning [string] in Python. When using str function you need put you text in quotations inside of the bracket==#     #
# ===================================================================================================================================

# True
# False

# print(True)
# print(False)

# print(type(True))

# ===================================================================================================================================
#      # ==Learning [string] in Python. When using str function you need put you text in quotations inside of the bracket==#     #
# ===================================================================================================================================

# blood_type = None

# print(blood_type)

# print(type(blood_type))

# print(len(blood_type))
# ==================================================================================================================================

# ==================================================================================================================================
# customer_name = "Moses Naworu"
# product_name = "Mac laptop"
# bill_paid = False
# price = 1500
# quantity = 4
# discount = 250
# print("total amount to be paid by the customer ", price*quantity-discount)
# =================================================================================================================================

# ---------------------------------------------------------------------------------------------------------------------------------
# =================================================================================================================================
# math = 70
# science = 40

# passing_score = 35

# if math >= passing_score and science >= passing_score:
#     print("test passed")
# else:
#     print("test failed")
# ================================================================================================================================

# --------------------------------------------------------------------------------------------------------------------------------
# ================================================================================================================================
# fruits = ["watermelon", "grapes", "oranges"]

# print("kiwi" in fruits)

# name = "jjtech"

# print("tech" in name)
# ================================================================================================================================

# ================================================================================================================================

# age = 50.5

# print(int(age))

# price = 10

# quantity = 2

# total = price * quantity

# print("Total amount to be paid: ", total)
# -----------------------------------------------------------------------------------------------------------------------------------
# ====================================================================================================================================

from imaplib import Int2AP


price = 20

quantity = int(input("how many items? "))
customer_name = "Moses"

print(type(quantity))

total = price * int(quantity)

print("Total amount to be paid: ", total)

quantity = quantity + 2

total = price * quantity

print("Total amount to be paid: ", total, "name: ",
      customer_name, "price", price, "quantity", quantity)

print("Total amount to be paid: ${}, customer name: {}, price: {}, quantity: {}".format(
    total, customer_name, price, quantity))
# ===========================================================================================================================================
