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

# print(20)    # =>int
# print(20.5)   # =>float
# print("number for number")   # =>str

#---------------------------------------------
# working with numbers: Arithmetic Operations
#=============================================

# --Different ways to write a python code to Calculate how many minutes in 20 days
#=================================================================================

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
######################################################################################################################
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

calculation_to_hours = 24   # Global and custom variables
name_of_unit_hours = "hours"  # Global and custom variables


def days_to_units(num_of_days):
    condition_check = num_of_days > 0  # use this to check data type
    print(type(condition_check))   # This called nested function
    print(num_of_days > 0)  # printing num_of_day >0 here will show if the user input is True of False
    if num_of_days > 0:    # here we are using a conditional function to prevent the user from using a negative number.
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit_hours}"
    elif num_of_days == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
        return "You have entered a 0, please enter a valid positive number"
    else:    # use the conditional else to return a message to the user
        return "No conversion for a negative number, please enter a positive number"


user_input = int(input("Hey User, enter a number of days and i will convert it to hours!\n"))  # convert here with int
user_input_number = int(user_input)  # This code can be run without this line

calculated_value = days_to_units(user_input)
print(calculated_value)