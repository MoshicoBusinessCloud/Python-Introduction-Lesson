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
from helper import validate_and_execute, user_input_message
# from helper import *   # The above function can also be writen this way
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)  # convert here with int
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute(days_and_unit_dictionary)

#======================================================================================================================