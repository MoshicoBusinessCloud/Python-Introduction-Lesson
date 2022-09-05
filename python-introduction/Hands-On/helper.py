# ======================================================================================================================
# ---------------------------------------------------------------------------------------------------
# #===Create a Module and Import Statement===#         #===Create a Module and Import Statement===#
# ---------------------------------------------------------------------------------------------------
# ======================================================================================================================
# ========================================
# Code[26.]
# ===========
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:  # Placing this condition here prevents users from entering a text or a float

        user_input_number = int(days_and_unit_dictionary["days"])  # This code can be run without this line

        # This part of the code is used to require users to enter only positive numbers
        if user_input_number > 0:  # This conditional function to prevent the user from using a negative number.
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:  # this condition is used to return a message to the user if they enter a 0 digit.
            print("You have entered a 0, please enter a valid positive number")
        else:
            print("No conversion for a negative number, please enter a positive number")

    except ValueError:
        print("Your input is not a valid number, please enter a valid number")


user_input_message = "Hey User, enter a number of days and conversion unit!\n"
#=======================================================================================================================
#=======================================================================================================================