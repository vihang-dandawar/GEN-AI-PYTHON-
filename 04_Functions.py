# def function_name(para1,para2): creating func
   #     body


# function_name(arg1,arg2)    calling func 

#Scopes
   # local: var inside a func & global

# enclosing func 
# def giveName():
#     name="vihang"
#     print(f"name is {name}")
#     def Anothername():
#         name="pranay"
#         print(f"name is {name}") # pranay

#     Anothername() # calling inner func
#     print(f"name is {name}\n\n\n") # outside inner func :vihang

#giveName()
# non local keyword can be used to acccess enclosing scope (inside upper level func not global) data 

name="kalpak"

def giveName():
    # nonlocal name error
    # global name correct
    name="vihang"
    print(f"name is {name}") # vihang
    def Anothername():
        nonlocal name
        # non local just looks for one lvel above the  current func for variables
        name="pranay" # global level var { name }is accessed and changed its value to pranay
        print(f"name is {name}") # pranay

    Anothername() # calling inner func
    print(f"name is {name}") # pranay
giveName()


def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

# 2 ways of passing args
make_chai("masala tea","amul milk","zero sugar")
make_chai(tea="masala tea",sugar="Zero",milk="amul") #  kwargs (keyword args)position doesn't matter 

def give_coffee(*ingredients,**extras): # variable args
    print(ingredients)
    print(extras)

give_coffee("sugar","milk","water",hot="yes",sweet="yes")
# for *param(ingredients) just give arg value
# for **param (extras) give key-value pairs


# types of functions
# pure vs impure (function that produces different outputs for the same inputs 
# over time or performs side effects)
# recursive
#lambda func


# Add chai types into new list if type !=kadak using lambda
chai_types=["masala","kadak","adrak","kadak"]
flitered_chai=list(filter(lambda chai: chai!="kadak",chai_types))
print(flitered_chai)

# we can provide defailt value to param in python
def hello(str="hii"):
    """hello this is documentation   of the func
     these are for developers to understand the code better"""
    return str

# built in function
#__doc__  documentation of function (dunder __)
#__name__  name of the function
print(hello.__doc__)
print(hello.__name__,"\n\n\n")

# import folder.file
# from folder.file import func as fc