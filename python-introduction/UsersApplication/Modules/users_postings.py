# ======================================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
# ##### Project Automation with Python ====CLASSES & OBJECTS==== Project Automation with Python ######
# ----------------------------------------------------------------------------------------------------------------------
# ======================================================================================================================
# Exercise 3 === Exercise 3 : Create another Class and Objects.
# =====================================================================================================================
# Version[5]: In this version of the code, we are going to create a Post module that is just a definition template
# and we are going to publish users postings on the users_main file; and then reference this Post module from the
# users_main file. By doing this we are changing the application from being monolithic. There are multiple way to call
# the module. Refer to the users_main file to see how we reference the module.
# =====================================================================================================================

class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author

    def get_post_info(self):
        print(f"Post: {self.message}, writen by {self.author}")