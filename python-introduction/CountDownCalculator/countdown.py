# ======================================================================================================================
# ---------------------------------------------------------------------------------------------------
#    #===Create a Module and Import Statement===#      #===Create a Module and Import Statement===#
# ---------------------------------------------------------------------------------------------------
# ======================================================================================================================
# ========================================
# Code[1]
# ===========

# import datetime
#
# user_input = input("Enter your goal with a deadline separated by colon\n")
# input_list = user_input.split(":")
#
#
# goal = input_list[0]
# deadline = input_list[1]
#
# print(datetime.datetime.strptime(deadline, "%d.%m.%y"))
#
# print(type(datetime.datetime.strptime(deadline, "%d.%m.%y")))

# ======================================================================================================================
# ---------------------------------------------------------------------------------------------------
#    #===Create a Module and Import Statement===#      #===Create a Module and Import Statement===#
# ---------------------------------------------------------------------------------------------------
# ======================================================================================================================
# ========================================
# Code[2]
# ===========

# import datetime
#
# user_input = input("Enter your goal with a deadline separated by colon\n")
# input_list = user_input.split(":")
#
#
# goal = input_list[0]
# deadline = input_list[1]
#
# deadline_date = datetime.datetime.strptime(deadline, "%m.%d.%y")
# today_date = datetime.datetime.today()
# #  calculate how many days from now till deadline
#
# print(deadline_date - today_date)

# ======================================================================================================================
# ---------------------------------------------------------------------------------------------------
#    #===Create a Module and Import Statement===#      #===Create a Module and Import Statement===#
# ---------------------------------------------------------------------------------------------------
# ======================================================================================================================
# ========================================
# Code[3]
# ===========

# import datetime
#
# user_input = input("Enter your goal with a deadline separated by colon\n")
# input_list = user_input.split(":")
#
#
# goal = input_list[0]
# deadline = input_list[1]
#
# deadline_date = datetime.datetime.strptime(deadline, "%m.%d.%y")
# today_date = datetime.datetime.today()
# time_till = deadline_date - today_date
# #  calculate how many days from now till deadline
#
# print(f"Dear User! Time remaining for you goal: {goal} is {time_till}")

# ======================================================================================================================
# ---------------------------------------------------------------------------------------------------
#    #===Create a Module and Import Statement===#      #===Create a Module and Import Statement===#
# ---------------------------------------------------------------------------------------------------
# ======================================================================================================================
# ========================================
# Code[4]
# ===========

# import datetime
#
# user_input = input("Enter your goal with a deadline separated by colon\n")
# input_list = user_input.split(":")
#
#
# goal = input_list[0]
# deadline = input_list[1]
#
# deadline_date = datetime.datetime.strptime(deadline, "%m.%d.%y")
# today_date = datetime.datetime.today()
# time_till = deadline_date - today_date
# #  calculate how many days from now till deadline
#
# print(f"Dear User! Time remaining for you goal: {goal} is {time_till.days} days")

# ======================================================================================================================
# ---------------------------------------------------------------------------------------------------
#    #===Create a Module and Import Statement===#      #===Create a Module and Import Statement===#
# ---------------------------------------------------------------------------------------------------
# ======================================================================================================================
# ========================================
# Code[5]
# ===========

# import datetime
#
# user_input = input("Enter your goal with a deadline separated by colon\n")
# input_list = user_input.split(":")
#
#
# goal = input_list[0]
# deadline = input_list[1]
#
# deadline_date = datetime.datetime.strptime(deadline, "%m.%d.%y")
# today_date = datetime.datetime.today()
# time_till = deadline_date - today_date
# #  calculate how many days from now till deadline
#
# hours_till = int(time_till.total_seconds() / 60 / 60)
#
# # print(f"Dear User! Time remaining for you goal: {goal} is {time_till}")
# # print(f"Dear User! Time remaining for you goal: {goal} is {time_till.days} days")
# # print(f"Dear User! Time remaining for you goal: {goal} is {time_till.total_seconds() / 60 / 60} hours")
# # print(f"Dear User! Time remaining for you goal: {goal} is {int(time_till.total_seconds() / 60 / 60)} hours")
# print(f"Dear User! Time remaining for you goal: {goal} is {hours_till} hours")

# ======================================================================================================================
# ---------------------------------------------------------------------------------------------------
#    #===Create a Module and Import Statement===#      #===Create a Module and Import Statement===#
# ---------------------------------------------------------------------------------------------------
# ======================================================================================================================
# ========================================
# Code[6]
# ===========

# from datetime import datetime
#
# user_input = input("Enter your goal with a deadline separated by colon\n")
# input_list = user_input.split(":")
#
# goal = input_list[0]
# deadline = input_list[1]
#
# deadline_date = datetime.strptime(deadline, "%m.%d.%y")
# today_date = datetime.today()
# time_till = deadline_date - today_date
# # calculate how many days from now till deadline
#
# hours_till = int(time_till.total_seconds() / 60 / 60)
#
# print(f"Dear User! Time remaining for you goal: {goal} is {hours_till} hours")

# ======================================================================================================================
# ---------------------------------------------------------------------------------------------------
# #===Module and Import Statement===#THIRD-PARTY PACKAGES #===Create a Module and Import Statement===#
# ---------------------------------------------------------------------------------------------------
# ======================================================================================================================
# ========================================
# Code[7]
# ===========

from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")


goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%m.%d.%y")
today_date = datetime.today()
time_till = deadline_date - today_date
#  calculate how many days from now till deadline

hours_till = int(time_till.total_seconds() / 60 / 60)


print(f"Dear User! Time remaining for you goal: {goal} is {hours_till} hours")
#======================================================================================================================================
#======================================================================================================================================