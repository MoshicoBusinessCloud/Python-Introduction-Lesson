# ======================================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
# ##### Project Automation with Python ====CLASSES & OBJECTS==== Project Automation with Python ######
# ----------------------------------------------------------------------------------------------------------------------
# ======================================================================================================================
# Exercise 2 === Exercise 2 : Create a Class User.
# ===================================================================================================================
# Version[3]: In this version of the code, we are going to create a User module that is just a definition template
# # and we are going to create the users attributes and behaviors on the users_main file; and then reference this User
# module from the users_main file. By doing this we are changing the application from being monolithic.
# There are multiple way to call the module. Refer to the users_main file to see how we reference the module.
# =====================================================================================================================

class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

# This is a dynamic class user behavior: nothing is hardcoded
    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

# Here we create our first user and the user was able to change their job title
    def get_user_info(self):
        print(f"user {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")