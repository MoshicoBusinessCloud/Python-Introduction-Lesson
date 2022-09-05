# ======================================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
# ##### Project Automation with Python ====CLASSES & OBJECTS==== Project Automation with Python ######
# ----------------------------------------------------------------------------------------------------------------------
# ======================================================================================================================
# Exercise 3 === Exercise 3 : Create another Class and Objects.
# =====================================================================================================================
# Version[5]: In this version of the code, we moved the user info to a different file and then we calling the user_app
# module from here. by doing this we are changing the application from being monolithic. There are multiple way to call
# the module, bellow is another way of calling a module. Here we are not importing only the class and not the whole
# module.
# =====================================================================================================================

from users_app import User
from users_post import Post

app_user_one = User("flyboy@coding.com", "FlyBoy John", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("Cloud Engineer")
app_user_one.get_user_info()

app_user_two = User("nanaboro@nash.com", "James Nanaboro", "safe_secrets", "Personal Trainer")
app_user_two.get_user_info()

app_user_two.change_job_title("Fitness Trainer")
app_user_two.get_user_info()

new_post = Post("On a mission to write some code today", app_user_one.name)
new_post.get_post_info()

new_post = Post("Going to train one of my client", app_user_two.name)
new_post.get_post_info()