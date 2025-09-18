# comprehensions are concise way to create lists,sets dict 
# using single line of code
# eg filters,trasnforming an obj ,creating new collections
# Types of Comprehensions:List,Set,Dict,,Generator

#-----------------------------------------------------
# List comprehension
print("list comprehensions")
# syntax

# list=[expression for item in items if condn]
menu=[

    "Masala chai","Ice chai","Green tea","Ginger tea","Coffee"
]
chai_not_tea=[mychai for mychai in menu if "chai" in mychai]
print(chai_not_tea,"\n\n\n")
# from types of tea/chai filter out chai not tea


#-------------------------------------------------
print("set comprehensions")
# set comprehensions
 # {} instead of [] for set (for unique)

numbers=[10,20,30,40,30,20,10,50,50]
unique_numbers={num for num in numbers if num>=20  }
print(unique_numbers)

# w/o if it will give all unique  with if unique obeying thee if condn

# consider you have a dict where key=type of tee,value=ingredients and you want ultimate list with all ingredients

recipes={
    "Masala Chai":["ginger","cardomon","clover"],
    "Elaichi Chai":["cardomon","milk"],
    "Masala Chai":["ginger","black pepper","clover"],

}

# in place of expression we write var name which is holding data that goes(eachingredients) into assigned list,set
unique_ingredients={  eachIngredient for ingredients in recipes.values() for eachIngredient in ingredients}
print(unique_ingredients ,"\n\n\n")

#--------------------------------------------------------
# if expression is key:value then it is dict or else everything same as set
tea_prices_inr={
    "masala tea":40,
    "green tea":50,
    "lemon tea":200
}

# convert to usd
# .items() give a key-value pair
# checkout expression key:value/80(for 1 usd=80 inr) 

tea_prices_usd={tea:price/80 for tea,price in tea_prices_inr.items() } # if can  also be written there
print(tea_prices_usd,"\n\n\n")



#----------------------------------------------------------------
# Generator
# same as list,set but memory  efficient it doesnt  directly create list,set  it is like a stream of data
# () instead  of [],{}
# you get one value at a time 
# syntax
# a=(x for x in items)
# you dont want value immedietely
# lazy evaluation
# yeild keyword
#yield is used inside a function to make it a generator.
# Instead of returning all values at once, it produces values one at a time,
#  pausing in between.Each time you call the generator (with next() or a loop), 
# execution resumes right after the last yield.

def giveNum():
    yield 1
    yield 4
    yield 7

getNum=giveNum() # just holding the referennce
print(giveNum()) #<function giveNum at 0x000001C6E2AA37E0>
print(getNum) #<generator object giveNum at 0x000001E4EFB75B10> 
print(next(getNum)) #1 only  generate 1st value
print(next(getNum)) #4  
print(next(getNum)) #7
#print(next(getNum),"\n\n\n") # error->stop Iteration

# Sending data to the yield

def chai_shop():
    print("welcome to the chai shop")
    order=yield
    while(True):
        print(f"prepearing {order}")
        order=yield


shop1=chai_shop()
next(shop1) # now reaching to first yeild

shop1.send("masala chai")


# yeild from another generator

def getValue():
    yield 21

def getValue2():
    try:
        while True:
            yield from getValue() # yielding from another generator
    except:
        print("closing the generator\n\n\n")
        

u2=getValue2()
print(next(u2))
u2.close() # closing the generator



#------------------------------------------------------------

# Decorators
# they are just wrapper around the function 

from functools import wraps
def myDecorator(func):
    @wraps(func) #Thanks to @wraps(func), metadata from the original hello is copied to wrapper
    def wrapper():
        print("Before func execution\n")
        func()
        print("After func execution")
    return wrapper

@myDecorator
def hello():
    """this func says hello to everybody"""
    print("Hello everybody\n")
   

hello()

print(hello.__name__)
print(hello.__doc__)

# if we dont use @wraps  then metadata like documentation .__doc__, ___name__ will not be copy to wrapper func


    

