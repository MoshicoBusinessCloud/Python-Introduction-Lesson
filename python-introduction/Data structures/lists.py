#  List will be helpful to store multiple items in a single variable.

"""
– Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
"""


# list variables
import re


fruits = ["banana", "apple", "watermelon", "kiwi", "grapes"]
prices = ["$100", "$150", "$10.50"]
numbers = [1, 2, 3, 4, 5]
my_list = [1, "car", 10.40, True]


# printing the list items

print('\n# printing the list items')
print(fruits, id(fruits))
print(prices)
print(numbers)
print(my_list)

# # # check the data type
print('\n# check the data type')
print(type(fruits))
print(type(numbers))
print(type(fruits[2]))


# # # nested list
print('\n# nested list')
my_custom_list = [fruits, prices, [6, 10, 2]]
print(my_custom_list)


# # # length of list
print('\n# length of the list')
print(len(fruits))

# # # access a specific element in list
print('\n# access a specific element in list')
print(fruits[2])
print(fruits[0])
print(fruits[-1])
print(fruits[-2])

# # # slicing lists
print('\n# slicing lists')
print(fruits[0:2])
print(fruits[1:4])
print(fruits[1:])


# # peform actions on list
# # return attributes and methods of an object
print('\n# dir() method')
print(dir(fruits))

# # modify particular index of list with new item
print('\n # modify particular index of list with new item')
print(prices)
prices[1] = '$1000'
print(prices)

# # # append items to existing list
print('\n# append() method')
fruits.append("mango")
print(fruits)

# # sort the list
print('\n# sort() the list')
fruits.sort()
fruits.sort(reverse=True)
print(fruits)

# # insert item at a particular index
print('\n# insert item at a particular index')
fruits.insert(1,'grapes')
print(fruits)

# remove an item from the list
print('\n# remove an item from the list')
fruits.remove('watermelon')
print(fruits)

# # iterate over all items in the list, one after another
print('\n# iterate over all items in the list, one after another')
for fruit in fruits:
    print(fruit)

# # iterate over each item in the list along with item index
print('\n# iterate over each item in the list along with item index')
for index, each_item in enumerate(fruits):
    print(index, each_item)

# # list with dictionaries inside
print('\n# list with dictionaries inside')
marks = [{"name": "vamsi", "marks": 50}, {"name": "avinash",
                                          "marks": 60}, {"name": "showmik", "marks": 70}, ]
print(marks)


# # clear a list
print('\n # clear a list')
fruits.clear()
print(fruits)

# # # delete the complete list
print('\n # delete the complete list')
del(fruits)
print(fruits)

###############################################################################################################################################
#==============================================================================================================================================
###############################################################################################################################################
# # printing the list items
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes'] 2740209726912
# ['$100', '$150', '$10.50']
# [1, 2, 3, 4, 5]
# [1, 'car', 10.4, True]

# # check the data type
# <class 'list'>
# <class 'list'>
# <class 'str'>

# # nested list
# [['banana', 'apple', 'watermelon', 'kiwi', 'grapes'], ['$100', '$150', '$10.50'], [6, 10, 2]]

# # length of the list
# 5

# # access a specific element in list
# watermelon
# banana
# grapes
# kiwi

# # slicing lists
# ['banana', 'apple']
# ['apple', 'watermelon', 'kiwi']
# ['apple', 'watermelon', 'kiwi', 'grapes']
# PS C:\Users\brown\python-introduction> & C:/Users/brown/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/brown/python-introduction/Data structures/lists.py"

# # printing the list items
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes'] 2110954419648
# ['$100', '$150', '$10.50']
# [1, 2, 3, 4, 5]
# [1, 'car', 10.4, True]

# # check the data type
# <class 'list'>
# <class 'list'>
# <class 'str'>

# # nested list
# [['banana', 'apple', 'watermelon', 'kiwi', 'grapes'], ['$100', '$150', '$10.50'], [6, 10, 2]]

# # length of the list
# 5

# # access a specific element in list
# watermelon
# banana
# grapes
# kiwi

# # slicing lists
# ['banana', 'apple']
# ['apple', 'watermelon', 'kiwi']
# ['apple', 'watermelon', 'kiwi', 'grapes']

# # dir() method
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# PS C:\Users\brown\python-introduction> & C:/Users/brown/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/brown/python-introduction/Data structures/lists.py"

# # printing the list items
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes'] 1810343278016
# ['$100', '$150', '$10.50']
# [1, 2, 3, 4, 5]
# [1, 'car', 10.4, True]

# # check the data type
# <class 'list'>
# <class 'list'>
# <class 'str'>

# # nested list
# [['banana', 'apple', 'watermelon', 'kiwi', 'grapes'], ['$100', '$150', '$10.50'], [6, 10, 2]]

# # length of the list
# 5

# # access a specific element in list
# watermelon
# banana
# grapes
# kiwi

# # slicing lists
# ['banana', 'apple']
# ['apple', 'watermelon', 'kiwi']
# ['apple', 'watermelon', 'kiwi', 'grapes']

# # dir() method
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#  # modify particular index of list with new item
# ['$100', '$150', '$10.50']
# ['$100', '$1000', '$10.50']
# PS C:\Users\brown\python-introduction> & C:/Users/brown/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/brown/python-introduction/Data structures/lists.py"

# # printing the list items
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes'] 2072703546816
# ['$100', '$150', '$10.50']
# [1, 2, 3, 4, 5]
# [1, 'car', 10.4, True]

# # check the data type
# <class 'list'>
# <class 'list'>
# <class 'str'>

# # nested list
# [['banana', 'apple', 'watermelon', 'kiwi', 'grapes'], ['$100', '$150', '$10.50'], [6, 10, 2]]

# # length of the list
# 5

# # access a specific element in list
# watermelon
# banana
# grapes
# kiwi

# # slicing lists
# ['banana', 'apple']
# ['apple', 'watermelon', 'kiwi']
# ['apple', 'watermelon', 'kiwi', 'grapes']

# # dir() method
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#  # modify particular index of list with new item
# ['$100', '$150', '$10.50']
# ['$100', '$1000', '$10.50']

# # append() method
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes', 'mango']

# # sort() the list
# ['apple', 'banana', 'grapes', 'kiwi', 'mango', 'watermelon']
# PS C:\Users\brown\python-introduction> & C:/Users/brown/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/brown/python-introduction/Data structures/lists.py"

# # printing the list items
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes'] 2498084422720
# ['$100', '$150', '$10.50']
# [1, 2, 3, 4, 5]
# [1, 'car', 10.4, True]

# # check the data type
# <class 'list'>
# <class 'list'>
# <class 'str'>

# # nested list
# [['banana', 'apple', 'watermelon', 'kiwi', 'grapes'], ['$100', '$150', '$10.50'], [6, 10, 2]]

# # length of the list
# 5

# # access a specific element in list
# watermelon
# banana
# grapes
# kiwi

# # slicing lists
# ['banana', 'apple']
# ['apple', 'watermelon', 'kiwi']
# ['apple', 'watermelon', 'kiwi', 'grapes']

# # dir() method
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#  # modify particular index of list with new item
# ['$100', '$150', '$10.50']
# ['$100', '$1000', '$10.50']

# # append() method
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes', 'mango']

# # sort() the list
# ['watermelon', 'mango', 'kiwi', 'grapes', 'banana', 'apple']
# PS C:\Users\brown\python-introduction> & C:/Users/brown/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/brown/python-introduction/Data structures/lists.py"

# # printing the list items
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes'] 1887653479744
# ['$100', '$150', '$10.50']
# [1, 2, 3, 4, 5]
# [1, 'car', 10.4, True]

# # check the data type
# <class 'list'>
# <class 'list'>
# <class 'str'>

# # nested list
# [['banana', 'apple', 'watermelon', 'kiwi', 'grapes'], ['$100', '$150', '$10.50'], [6, 10, 2]]

# # length of the list
# 5

# # access a specific element in list
# watermelon
# banana
# grapes
# kiwi

# # slicing lists
# ['banana', 'apple']
# ['apple', 'watermelon', 'kiwi']
# ['apple', 'watermelon', 'kiwi', 'grapes']

# # dir() method
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#  # modify particular index of list with new item
# ['$100', '$150', '$10.50']
# ['$100', '$1000', '$10.50']

# # append() method
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes', 'mango']

# # sort() the list
# ['watermelon', 'mango', 'kiwi', 'grapes', 'banana', 'apple']

# # insert item at a particular index
# ['watermelon', 'grapes', 'mango', 'kiwi', 'grapes', 'banana', 'apple']

# # remove an item from the list
# ['grapes', 'mango', 'kiwi', 'grapes', 'banana', 'apple']
# PS C:\Users\brown\python-introduction> & C:/Users/brown/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/brown/python-introduction/Data structures/lists.py"

# # printing the list items
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes'] 2329413830080
# ['$100', '$150', '$10.50']
# [1, 2, 3, 4, 5]
# [1, 'car', 10.4, True]

# # check the data type
# <class 'list'>
# <class 'list'>
# <class 'str'>

# # nested list
# [['banana', 'apple', 'watermelon', 'kiwi', 'grapes'], ['$100', '$150', '$10.50'], [6, 10, 2]]

# # length of the list
# 5

# # access a specific element in list
# watermelon
# banana
# grapes
# kiwi

# # slicing lists
# ['banana', 'apple']
# ['apple', 'watermelon', 'kiwi']
# ['apple', 'watermelon', 'kiwi', 'grapes']

# # dir() method
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#  # modify particular index of list with new item
# ['$100', '$150', '$10.50']
# ['$100', '$1000', '$10.50']

# # append() method
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes', 'mango']

# # sort() the list
# ['watermelon', 'mango', 'kiwi', 'grapes', 'banana', 'apple']

# # insert item at a particular index
# ['watermelon', 'grapes', 'mango', 'kiwi', 'grapes', 'banana', 'apple']

# # remove an item from the list
# ['grapes', 'mango', 'kiwi', 'grapes', 'banana', 'apple']

# # iterate over all items in the list, one after another
# grapes
# mango
# kiwi
# grapes
# banana
# apple
# PS C:\Users\brown\python-introduction> & C:/Users/brown/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/brown/python-introduction/Data structures/lists.py"

# # printing the list items
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes'] 2786398979456
# ['$100', '$150', '$10.50']
# [1, 2, 3, 4, 5]
# [1, 'car', 10.4, True]

# # check the data type
# <class 'list'>
# <class 'list'>
# <class 'str'>

# # nested list
# [['banana', 'apple', 'watermelon', 'kiwi', 'grapes'], ['$100', '$150', '$10.50'], [6, 10, 2]]

# # length of the list
# 5

# # access a specific element in list
# watermelon
# banana
# grapes
# kiwi

# # slicing lists
# ['banana', 'apple']
# ['apple', 'watermelon', 'kiwi']
# ['apple', 'watermelon', 'kiwi', 'grapes']

# # dir() method
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#  # modify particular index of list with new item
# ['$100', '$150', '$10.50']
# ['$100', '$1000', '$10.50']

# # append() method
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes', 'mango']

# # sort() the list
# ['watermelon', 'mango', 'kiwi', 'grapes', 'banana', 'apple']

# # insert item at a particular index
# ['watermelon', 'grapes', 'mango', 'kiwi', 'grapes', 'banana', 'apple']

# # remove an item from the list
# ['grapes', 'mango', 'kiwi', 'grapes', 'banana', 'apple']

# # iterate over all items in the list, one after another
# grapes
# mango
# kiwi
# grapes
# banana
# apple

# # iterate over each item in the list along with item index
# 0 grapes
# 1 mango
# 2 kiwi
# 3 grapes
# 4 banana
# 5 apple
# PS C:\Users\brown\python-introduction> & C:/Users/brown/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/brown/python-introduction/Data structures/lists.py"

# # printing the list items
# ['banana', 'apple', 'watermelon', 'kiwi', 'grapes'] 2217805695488
# ['$100', '$150', '$10.50']
# [1, 2, 3, 4, 5]
# [1, 'car', 10.4, True]

# # check the data type
# <class 'list'>
# <class 'list'>
# <class 'str'>

# # nested list
# [['banana', 'apple', 'watermelon', 'kiwi', 'grapes'], ['$100', '$150', '$10.50'], [6, 10, 2]]

# # length of the list
# 5

# # access a specific element in list
# watermelon
# banana
# grapes
# kiwi

# # slicing lists
# ['banana', 'apple']
# ['apple', 'watermelon', 'kiwi']
# ['apple', 'watermelon', 'kiwi', 'grapes']

# # dir() method
# 1 mango2 kiwi3 grapes4 banana
# 5 apple

# # list with dictionaries inside
# [{'name': 'vamsi', 'marks': 50}, {'name': 'avinash', 'marks': 60}, {'name': 'showmik', 'marks': 70}]
# PS C:\Users\brown\python-introduction>