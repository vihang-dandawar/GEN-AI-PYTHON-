print("hello")
print(2+3)
import sys
print(sys.version)
a=10
b=15
print(a/b) #0.6666
print(a//b) # 0 ignores values after decimal


# power function in python a**b
#2**3=>2*2*2


# can write billion in this way to improve readibility
# 1_000_000_000
print(1_000_000_000)



# -------Boolean ---------------
isOk=True # True=1-> upcasting, False=0-> downcasting
print(1+True) # output=2

milk_present=1
print(f"is milk present? {bool(milk_present)}") # output =true


milk_present=12 # except 0,None most values numbers ,string are truthy values
print(f"is milk present? {bool(milk_present)}") # output =true

 
# logical operator=> and ,or ,not


# float library
from fractions import Fraction
from decimal import Decimal

#------------------------------------------------
#String
chai_type="Masala*Chai"
customer_name="Priya"
print(f"Order for {customer_name} {chai_type} please!")
# in indexing last number is excluded (0,6) masala

print(f"Indexing for {chai_type[0:6:2]}") # Masala

# [0:6:2] between 0-6  and skip every 2nd letter

print(f"Indexing for {chai_type[::-1]}") # string is reversed

#------------------------------------------------
# tuples
# ()<- tuples symbol
sports=("cricket","kabaddi","kho-kho")
print(f"sports list is {sports}")

# we cannot add new entry in tuple-> immutable

(game1,game2,game3)=sports
print(f"game 1 and game 2 are  {game1},{game2}")

a,b=10,20 # a=10,b=20
print(f"value of a {a}") #=>10

a,b=b,a # swapping a with b
print(f"value of a after swap {a}") #a=20

# membership
print(f"is cricket listed as a sport {'cricket' in sports}")

# checking if given is member of tuple or not
#{'abc' in tuple_name} returns  true/false
# abc  -> case sensitive mention precisely


#-------mutable------------------------------------
#1)List
#Array in (cpp,java)=List(python)

cricket=["virat","rohit","ms"]
print(cricket)


 # You cannot directly add an element into an existing tuple because tuples are immutable in Python.
 # for List you can direct append

cricket.append("Abd")
print(cricket)

football=["cr7","messi","mbappe","neymar"]
cricket.extend(football)  # cricket=cricket+football
play=cricket
print(f"merged player {play}")
cricket.insert(3,"raina")
print(cricket) # .insert(idx,value)
cricket.remove("ms") # remove by value
removed_player=cricket.pop() # remove last and return the value
print(cricket,removed_player)
#cricket.reverse()
# cricket.sort() internally implement timsort(merged+insertion)
print(cricket)

numbers=[2,3,4,1,7,3]
print(max(numbers)) # max function returns max from any arr
print(min(numbers)) # min function returns min from any arr


# operator overloading= list=list1 + list2 
numbers*=3# list is created 3 times
print(numbers) #[2, 3, 4, 1, 7, 3, 2, 3, 4, 1, 7, 3, 2, 3, 4, 1, 7, 3]

from operator import itemgetter


#Set----------------------------------------------
# {}->set  contains unique

num1={1,2,3,5,6}
num2={3,5,6,7,8,9}
num=num1 | num2  #union  
num3=num1 & num2 # intersection
num4=num1-num2 # only in num1 not both 
print("union of num1 and num2 ",num)
print("intersection of num1 and num2 ",num3)
print("only in num1 and not in  num2 ",num4)

print("\n\n\n\n")


print("Dictionary")
# Dictionary ---------------------------------------
 # key-value pair
 # name based indexing
 # order doesnt matter
my_info=dict(name="vihang",age=21,status="single")
my_info["life"]="peaceful" # way of adding key-value in dict
del my_info["life"] # way of deleting key-value from dict

print("Keys: ",my_info.keys())
print( "Values :", my_info.values())
print("All items ",my_info.items())

new_info=dict(year="BE",placed="not yet")
my_info.update(new_info)
print(my_info)# update current list by adding new list

print(my_info.get("salary","Not employed yet")) 
# there is no entry by "salary" so in such case we can provide defaults
# prevents error and doesnt crash
print("\n\n\n")


# Advanced data types------------------------

#datetime, time, calender, timedelta, arrow, dateutils
