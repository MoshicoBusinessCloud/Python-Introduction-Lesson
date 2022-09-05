
# age = 20
# age = 30
# price = 19.50
# first_name = "Moses"
# last_name = "Naworu"
# is_online = False
# print("New Patient")
# print("age", "first", "last")
# print(age,first_name,last_name)
#=========================================
# IDE --Integrated Development Environment
#=========================================
#================================================================================================
# Data type: string[text], integer[numbers], float[decimer numbers], bloolean[True or False]
#================================================================================================

#========================================
# String and numbers
#========================================
# Code[1]
#===========

# print(20)    # =>int
# print(20.5)   # =>float
# print("number for number")   # =>str

#---------------------------------------------
# working with numbers: Arithmetic Operations
#=============================================

# --Different ways to write a python code to Calculate how many minutes in 20 days
#=================================================================================
#========================================
# Code[2]
#===========
# print(20 * 24 * 60)
# print("20 days are XXX minutes")
# # print("20 days are" + XXX + "minutes")
# print("20 days are" + str(50) + "minutes")
# print("20 days are " + str(50) + " minutes")
# print(f"50 days are {50} minutes")
# print(f"20 days are {20 * 24 * 60} minutes")
# print(f"35 days are {35 * 24 * 60} minutes")
# print(f"100 days are {100 * 24 * 60} minutes")
# print(f"50 days are {50 * 24 * 60 * 60} seconds")
# print(f"60 days are {60 * 24 * 60 * 60} seconds")
# print(f"20 days are {20 * 24 * 60 * 60} seconds")

#---------------------------------------------------------------------------------
# creating custom and descriptive variables when writing your code
#=================================================================================
#========================================
# Code[3]
#===========
# calculation_to_hours = 24
# calculation_to_minutes = 24 * 60
# calculation_to_seconds = 24 * 60 * 60
# name_of_unit = "seconds"
# name_of_unit_minutes = "minutes"
# name_of_unit_hours = "hours"
#
# print(f"35 days are {35 * calculation_to_minutes} minutes")
# print(f"100 days are {100 * calculation_to_minutes} minutes")
# print(f"50 days are {50 * calculation_to_seconds} seconds")
# print(f"20 days are {20 * calculation_to_seconds} seconds")
#
# print(f"35 days are {35 * calculation_to_hours} hours")
# print(f"100 days are {100 * calculation_to_hours} hours")
# print(f"35 days are {35 * calculation_to_hours} {name_of_unit_hours}")
# print(f"100 days are {100 * calculation_to_hours} {name_of_unit_hours}")
#
# print(f"35 days are {35 * calculation_to_minutes} {name_of_unit_minutes}")
# print(f"100 days are {100 * calculation_to_minutes} {name_of_unit_minutes}")
# print(f"50 days are {50 * calculation_to_seconds} {name_of_unit}")
# print(f"20 days are {20 * calculation_to_seconds} {name_of_unit}")

#=============================================================================================================
# How to create functions when writing python code
#=============================================================================================================
#========================================
# Code[4]
#===========
# calculation_to_hours = 24
# calculation_to_minutes = 24 * 60
# calculation_to_seconds = 24 * 60 * 60
# name_of_unit = "seconds"
# name_of_unit_minutes = "minutes"
# name_of_unit_hours = "hours"


# def days_to_unit():
#     print(f"20 days are {20 * calculation_to_seconds} {name_of_unit}")
#     print(f"100 days are {100 * calculation_to_minutes} {name_of_unit_minutes}")
#     print("It's All Good!")
#
#
# days_to_unit()
#------------------------------------------------------------------------------------------------------------------
#========================================
# Code[5]
#===========
# calculation_to_hours = 24
# calculation_to_minutes = 24 * 60
# calculation_to_seconds = 24 * 60 * 60
# name_of_unit = "seconds"
# name_of_unit_minutes = "minutes"
# name_of_unit_hours = "hours"
#
#
# def days_to_units(num_of_days):
#     print(f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}")
#     print("It's All Good!")
#
#
# days_to_units(20)
# days_to_units(35)
# days_to_units(60)
# days_to_units(100)
#
#
# def days_to_units(num_of_days):
#     print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}")
#     print("It's All Good!")
#
#
# days_to_units(20)
# days_to_units(35)
# days_to_units(60)
# days_to_units(100)
#
#
# def days_to_units(num_of_days):
#     print(f"{num_of_days} days are {num_of_days * calculation_to_minutes} {name_of_unit_minutes}")
#     print("It's All Good!")
#
#
# days_to_units(20)
# days_to_units(35)
# days_to_units(60)
# days_to_units(100)

#==================================================================================================================
# You will get an error if you do not give your function a value after making your code dynamic
#------------------------------------------------------------------------------------------------------------------
#========================================
# Code[6]
#===========
# calculation_to_hours = 24
# name_of_unit_hours = "hours"
#
#
# def days_to_units(num_of_days):
#     print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}")
#     print("It's All Good!")
#
#
# days_to_units()

#=================================================================================================================
# Dynamic function === Avoiding Hard Coding === using parameter to call the variables
#=================================================================================================================
#========================================
# Code[7]
#===========
# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days, custom_message):  # (Local variables) here we are using 2 variables inside the function
#     print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}")
#     print(custom_message)   # variable parameter
#
#
# days_to_units(35, "It's All Good!")  # if you have 2 local variables in you function, you must have 2 values as well
# days_to_units(60, "Happy About The Calculation!")

#===============================================================================================================
# Variable Scope in function== A variable is only available from inside the region it is created
# ---Global Scope = variables available from within any scope
# ---Local Scope = variables created inside function can only be used inside of that function
#=================================================================================================================
#========================================
# Code[8]
#===========
# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days, custom_message):  # (Local variables) here we are using 2 variables inside the function
#     print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}")
#     print(custom_message)   # variable parameter
#
#
# def scope_check():
#     print(name_of_unit_hours)  # The [Global] variable above works here
#     print(num_of_days)  # But the [Local] or internal variable in another function can not be used here [This is bad]
#
#
# scope_check()
#
# days_to_units(35, "It's All Good!")  # if you have 2 local variables in you function, you must have 2 values as well
# days_to_units(60, "Happy About The Calculation!")

#---------------------------------------------------------------------------------------------------------------------
# The Example below has 1 [Global variable] and 2 [Local or internal variables]
#=====================================================================================================================
#========================================
# Code[9]
#===========
# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days, custom_message):  # (Local variables) here we are using 2 variables inside the function
#     print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}")
#     print(custom_message)   # variable parameter
#
#
# def scope_check(num_of_days):  # to solve the above issue you have to create a local variable in the function
#     my_var = "variable inside function"  # This is another way to write internal or local variables
#     print(name_of_unit_hours)  # The [Global] variable above works here
#     print(num_of_days)  # But the [Local] or internal variable in another function can not be used here [This is bad]
#     print(my_var) # here we are printing the above variable


# scope_check( 20)  # here we are providing a value for the above function
#
# days_to_units(35, "It's All Good!")  # if you have 2 local variables in you function, you must have 2 values as well
# days_to_units(60, "Happy About The Calculation!")

#======================================================================================================================
#================================================================
# User input
#================================================================
#======================================================================================================================
#==========================================
# Code[10]
#===========
# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days):
#     print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}")
#     print("It's All Good!")
#
#
# user_input = input("Hey User, enter a number of days and i will convert it to hours!\n")
# print(user_input)

#=====================================================================================================================
#----------------------------------------------
# Function with Return Values
# with return value function, you need to create a variable the equal function and then print the variable
#----------------------------------------------
#=====================================================================================================================
#========================================
# Code[11]
#===========
# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"
#
#
# my_ver = days_to_units(20)
# print(my_ver)
#--------------------------------------------------------------------------------------------------------------------
#========================================
# Code[12]
#===========
# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"
#
#
# user_input = int(input("Hey User, enter a number of days and i will convert it to hours!\n"))  # convert here with int
# user_input_number = int(user_input)  # This code can be run without this line
#
# calculated_value = days_to_units(user_input)
# print(calculated_value)

#======================================================================================================================
#######################################################################################################################
# Conditionals (if / else) & Boolean Data Type || We want avoid Invalid user input by placing restriction on user input
# Conditionals === Expressions that evaluate to either true or false
#---------------------------------------------------------------------------------------------------------------------
#========================================
# Code[13]
#===========
# # Equals: a == b
# # Not Equals: a != b
# # Less than: a < b
# # Less than or equal to: a <= b
# # Greater than: a > b
# # Greater than or equal to: a >= b
#===========================================
# THE FLOW
# user give input -->input is converted into integer -->it is passed to days_to_units function -->It is then passed
# through if condition to check if the user input is greater or lesser than 0 -->If the user input is > 0, it will
# perform the calculation. else: it will print a default message

# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days):
#     condition_check = num_of_days > 0  # use this to check data type
#     print(type(condition_check))   # This called nested function
#     print(num_of_days > 0)  # printing num_of_day >0 here will show if the user input is True of False
#     if num_of_days > 0:    # here we are using a conditional function to prevent the user from using a negative number.
#         return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"
#     elif num_of_days == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
#         return "You have entered a 0, please enter a valid positive number"
#     else:    # use the conditional else to return a message to the user
#         return "No conversion for a negative number, please enter a positive number"
#
#
# user_input = int(input("Hey User, enter a number of days and i will convert it to hours!\n"))  # convert here with int
# user_input_number = int(user_input)  # This code can be run without this line
#
# calculated_value = days_to_units(user_input)
# print(calculated_value)

#===================================================================================================================
#-----------------------------------------
# MORE USER INPUT VALIDATION
#-----------------------------------------
#===================================================================================================================
#========================================
# Code[14]
#===========
# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days):
#     condition_check = num_of_days > 0  # use this to check data type
#     print(type(condition_check))   # This called nested function
#     print(num_of_days > 0)  # printing num_of_day >0 here will show if the user input is True of False
#     if num_of_days > 0:    # here we are using a conditional function to prevent the user from using a negative number.
#         return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"
#     elif num_of_days == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
#         return "You have entered a 0, please enter a valid positive number"
#     else:    # use the conditional else to return a message to the user  # We also don't need the else
#     # condition because isdigit function also filtered out negative numbers.
#         return "No conversion for a negative number, please enter a positive number"
#
#
# user_input = input("Hey User, enter a number of days and i will convert it to hours!\n")  # convert here with int
#
# if user_input.isdigit():  # Placing this condition here prevents users from entering a text or a float
#     user_input_number = int(user_input)  # This code can be run without this line
#     calculated_value = days_to_units(user_input_number)
#     print(calculated_value)
# else:
#     print("Your input is not a valid number, please enter a valid number")

#======================================================================================================================
#-----------------------------------------------------------
# CLEAN UP OUR CODE === A BETTER WAY TO WRITE THE ABOVE CODE
#-----------------------------------------------------------
#======================================================================================================================
#========================================
# Code[15]
#===========
# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days):
#     if num_of_days > 0:    # here we are using a conditional function to prevent the user from using a negative number.
#         return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"
#     elif num_of_days == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
#         return "You have entered a 0, please enter a valid positive number"
#
#
# def validate_and_execute():
#     if user_input.isdigit():  # Placing this condition here prevents users from entering a text or a float
#         user_input_number = int(user_input)  # This code can be run without this line
#         calculated_value = days_to_units(user_input_number)
#         print(calculated_value)
#     else:
#         print("Your input is not a valid number, please enter a valid number")
#
#
# user_input = input("Hey User, enter a number of days and i will convert it to hours!\n")  # convert here with int
# validate_and_execute()


#======================================================================================================================
#-------------------------------------------------------
# ====== NESTED If ....Else
#-------------------------------------------------------
#======================================================================================================================
#========================================
# Code[16]
#===========
# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"
#
#
# def validate_and_execute():
#     if user_input.isdigit():  # Placing this condition here prevents users from entering a text or a float
#         user_input_number = int(user_input)  # This code can be run without this line
#         if user_input_number > 0:  # This conditional function to prevent the user from using a negative number.
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
#             print("You have entered a 0, please enter a valid positive number")
#     else:
#         print("Your input is not a valid number, please enter a valid number")
#
#
# user_input = input("Hey User, enter a number of days and i will convert it to hours!\n")  # convert here with int
# validate_and_execute()

#======================================================================================================================
#----------------------------------------------------
# ===== Error Handling with try / except =====#
#----------------------------------------------------
#======================================================================================================================
#========================================
# Code[17]
#===========
# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"
#
#
# def validate_and_execute():
#     try: # Placing this condition here prevents users from entering a text or a float
#
#         user_input_number = int(user_input)   # This code can be run without this line
#         if user_input_number > 0:  # This conditional function to prevent the user from using a negative number.
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
#             print("You have entered a 0, please enter a valid positive number")
#         else:
#             print("No conversion for a negative number, please enter a positive number")
#
#     except ValueError:
#         print("Your input is not a valid number, please enter a valid number")
#
#
# user_input = input("Hey User, enter a number of days and i will convert it to hours!\n")  # convert here with int
# validate_and_execute()

#======================================================================================================================
#----------------------------------------------------
# ===== Python While Loops =====#
#----------------------------------------------------
#======================================================================================================================
#========================================
# Code[18]
#===========
# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"
#
#
# def validate_and_execute():
#     try: # Placing this condition here prevents users from entering a text or a float
#
#         user_input_number = int(user_input)   # This code can be run without this line
#         if user_input_number > 0:  # This conditional function to prevent the user from using a negative number.
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
#             print("You have entered a 0, please enter a valid positive number")
#         else:
#             print("No conversion for a negative number, please enter a positive number")
#
#     except ValueError:
#         print("Your input is not a valid number, please enter a valid number")
#
# while True:
#     user_input = input("Hey User, enter a number of days and i will convert it to hours!\n")  # convert here with int
#     validate_and_execute()

#======================================================================================================================
#-------------------------------------
# A Way to let users exit the program
#-------------------------------------
#======================================================================================================================
#========================================
# Code[19]
#===========
calculation_to_hours = 24   # Global and custom variables
name_of_unit_hours = "hours"  # Global and custom variables


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"


def validate_and_execute():
    try: # Placing this condition here prevents users from entering a text or a float

        user_input_number = int(user_input)   # This code can be run without this line
        if user_input_number > 0:  # This conditional function to prevent the user from using a negative number.
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
            print("You have entered a 0, please enter a valid positive number")
        else:
            print("No conversion for a negative number, please enter a positive number")

    except ValueError:
        print("Your input is not a valid number, please enter a valid number")


user_input = ""
while user_input != "exit":
    user_input = input("Hey User, enter a number of days and i will convert it to hours!\n")  # convert here with int
    validate_and_execute()
    
#======================================================================================================================
#-----------------------------------------------
# ===List & For Loop====# List for loop allows you to enter multiple values at one time instead of doing so one by one=#
#-----------------------------------------------
#======================================================================================================================
#========================================
# Code[20]
#===========
# calculation_to_hours = 24   # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"
#
#
# def validate_and_execute():
#     try: # Placing this condition here prevents users from entering a text or a float
#
#         user_input_number = int(num_of_days_element)   # This code can be run without this line
#         if user_input_number > 0:  # This conditional function to prevent the user from using a negative number.
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
#             print("You have entered a 0, please enter a valid positive number")
#         else:
#             print("No conversion for a negative number, please enter a positive number")
#
#     except ValueError:
#         print("Your input is not a valid number, please enter a valid number")
#
#
# user_input = ""
# while user_input != "exit":
#     user_input = input("Hey User, enter number of days as a comma separated list and i will convert it to hours!\n")
#     for num_of_days_element in user_input.split(", "):
#         validate_and_execute()
#======================================================================================================================
#-----------------------------------------------
# ===List & For Loop====# List & for loop Continue
#-----------------------------------------------
#======================================================================================================================
#========================================
# Code[21]
#===========
# calculation_to_hours = 24  # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"
#
#
# def validate_and_execute():
#     try:  # Placing this condition here prevents users from entering a text or a float
#
#         user_input_number = int(num_of_days_element)  # This code can be run without this line
#
#         # This part of the code is use to require users to enter only positive numbers
#         if user_input_number > 0:  # This conditional function to prevent the user from using a negative number.
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
#             print("You have entered a 0, please enter a valid positive number")
#         else:
#             print("No conversion for a negative number, please enter a positive number")
#
#     except ValueError:
#         print("Your input is not a valid number, please enter a valid number")
#
#
# user_input = ""
# while user_input != "exit":
#     user_input = input("Hey User, enter a number of days and i will convert it to hours!\n")  # convert here with int
#     print(type(user_input.split(", ")))
#     print(user_input.split(", "))
#     for num_of_days_element in user_input.split(", "):
#         validate_and_execute()

#======================================================================================================================
#-----------------------------------------------
# ===List & For Loop====# List & for loop Continue
#-----------------------------------------------
#======================================================================================================================
#========================================
# Code[22]
#===========
# calculation_to_hours = 24  # Global and custom variables
# name_of_unit_hours = "hours"  # Global and custom variables
#
#
# def days_to_units(num_of_days):
#     return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"
#
#
# def validate_and_execute():
#     try:  # Placing this condition here prevents users from entering a text or a float
#
#         user_input_number = int(num_of_days_element)  # This code can be run without this line
#
#         # This part of the code is use to require users to enter only positive numbers
#         if user_input_number > 0:  # This conditional function to prevent the user from using a negative number.
#             calculated_value = days_to_units(user_input_number)
#             print(calculated_value)
#         elif user_input_number == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
#             print("You have entered a 0, please enter a valid positive number")
#         else:
#             print("No conversion for a negative number, please enter a positive number")
#
#     except ValueError:
#         print("Your input is not a valid number, please enter a valid number")
#
#
# user_input = ""
# while user_input != "exit":
#     user_input = input("Hey User, enter a number of days and i will convert it to hours!\n")  # convert here with int
#     list_of_days = user_input.split(", ")
#     print(list_of_days)
#     print(set(list_of_days))
#
#     print(type(list_of_days))
#     print(type(set(list_of_days)))
#
#     for num_of_days_element in set(list_of_days):
#         validate_and_execute()

# ======================================================================================================================
# -----------------------------------------------
# ===Basic Set Operations and Syntax ====#
# -----------------------------------------------
# ======================================================================================================================
# ========================================
# Code[23]
# ===========
# my_set = {"January", "February", "March", "April", "May", "June", "February"}
# for element in my_set:
#     print(element)
#
# my_set.add("August")
# print(my_set)
# my_set.remove("April")
# print(my_set)
#
# my_list = ["January", "February", "March", "April", "May", "June", "February"]
# my_list.remove("February")
# print(my_list)
# my_list.append("February")
# print(my_list)

# ======================================================================================================================
# ---------------------------------------------------------------------------------------------------------------
# ===Built in Function ====# Custom Function ==# Function #fUNCTIONS CALLED DIRECTLY ON A VALUE ===#
# ===Different Data Type ===#  # ===All the data type we have used thus far ===#  # ===Different Data Type ===#
# --------------------------------------------------------------------------------------------------------------
# ======================================================================================================================
# ========================================
# Code[24.]
# ===========
# DIFFERENT TYPES OF FUNCTIONS USED IN OUR LEARNING THUS FAR:

# BUILT IN FUNCTIONS:
# print()
# input()
# int()
# set()

# CUSTOM FUNCTIONS:
# def days_to_units():
# def validate_and_execute():

# fUNCTIONS CALLED DIRECTLY ON A VALUE:
# The difference between this function and the other
# built-in function: with this type of function, each
# data type have its own type or list of functions.

# "test".split()
# "February".capitalize()
# "February".find()
# [2, 3, 9,].index()
# [2, 3, 9,].count()
# [2, 3, 9,].append()

# DIFFERENT DATA TYPE:

# str_message = "enter a value"
# int_days = 20
# float_price = 9.99
# bool_valid_number = True
# boll_exit_input = False
# list_of_days = [20, 30, 40, 50, 60]
# list_of_months = ["January", "February", "March"]
# set_of_days = {10, 20, 30, 40}
# dictionary_days_and_unit = {"days": 10, "unit": "hours"}


# ======================================================================================================================
# ---------------------------------------------------------------------------------------------------
# ===Dictionary Data Type ===#
# ---------------------------------------------------------------------------------------------------
# ======================================================================================================================
# ========================================
# Code[25.]
# ===========

# def days_to_units(num_of_days, conversion_unit):
#     if conversion_unit == "hours":
#         return f"{num_of_days} days are {num_of_days * 24} hours"
#     elif conversion_unit == "minutes":
#         return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
#     else:
#         return "unsupported unit"
#
#
# def validate_and_execute():
#     try:  # Placing this condition here prevents users from entering a text or a float
#
#         user_input_number = int(days_and_unit_dictionary["days"])  # This code can be run without this line
#
#         # This part of the code is use to require users to enter only positive numbers
#         if user_input_number > 0:  # This conditional function to prevent the user from using a negative number.
#             calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
#             print(calculated_value)
#         elif user_input_number == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
#             print("You have entered a 0, please enter a valid positive number")
#         else:
#             print("No conversion for a negative number, please enter a positive number")
#
#     except ValueError:
#         print("Your input is not a valid number, please enter a valid number")
#
#
# user_input = ""
# while user_input != "exit":
#     user_input = input("Hey User, enter a number of days and conversion unit!\n")  # convert here with int
#     days_and_unit = user_input.split(":")
#     print(days_and_unit)
#     days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
#     print(days_and_unit_dictionary)
#     print(type(days_and_unit_dictionary))
#     validate_and_execute()
# ----------------------------------------------------------------------------------------------------------------------

# my_list = ["10", "20", "100", "200"]
# print(my_list[1])
#
# my_dictionary = {"days": 100, "unit": "hours", "message": "Look, I'm learning Python"}
# print(my_dictionary["message"])

# ======================================================================================================================
# ---------------------------------------------------------------------------------------------------
# #===MODULES===#  #===MODULES===#  #===MODULES===#  #===MODULES===#  #===MODULES===#  #===MODULES===#
# ---------------------------------------------------------------------------------------------------
# ======================================================================================================================
# ========================================
# Code[26.]
# ===========
# This is one way of calling or referencing modules
# import helper
#
# user_input = ""
# while user_input != "exit":
#     user_input = input(helper.user_input_message)  # convert here with int
#     days_and_unit = user_input.split(":")
#     print(days_and_unit)
#     days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
#     print(days_and_unit_dictionary)
#     print(type(days_and_unit_dictionary))
#     helper.validate_and_execute(days_and_unit_dictionary)

#-----------------------------------------------------------------------------------------------------------------------
# ===The above module can also be writen this way
#-----------------------------------------------------------------------------------------------------------------------
# from helper import validate_and_execute, user_input_message
# # from helper import *   # The above function can also be writen this way
# user_input = ""
# while user_input != "exit":
#     user_input = input(user_input_message)  # convert here with int
#     days_and_unit = user_input.split(":")
#     print(days_and_unit)
#     days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
#     print(days_and_unit_dictionary)
#     print(type(days_and_unit_dictionary))
#     validate_and_execute(days_and_unit_dictionary)

#======================================================================================================================