for token in range(1,6):
    print(f"token no:{token}") # range(1,6)  6 is exclusive ->1,2,3,4,5 reps

customer_name=["vikki", "ajay","aman","aj","ak"]
for name in customer_name: # looping over list of names like for-each
    print(f"order ready for {name}")

# enumerate
# it gives value and idx access from a list we can choose by which value to initialize idx

for idx,name in enumerate(customer_name,start=10): 
    print(f" name {idx} is {name}")# 10:vikki, 11:ajay,12:aman

# use zip to iterate over mutiple iterable items

# here it is shown using two list name and age
age=[22,23,25,21,26]

for age,names in zip(age,customer_name):
    print(f"User name and age are:{name}:{age}")

# while loop
temperature=50
while temperature<100:
    print(f"temperature is increasing...{temperature}")
    temperature+=15
print(" high temperature stops boiling..\n\n\n")


#customer_name=["vikki", "ajay","aman","aj","ak"]
for names in customer_name:
    if(names=="aman"): # skip  everything for this pass when name=aman
        continue
    if(names=="aj"): # when name=aj comes break through loop
        break
    print(names)
print("outside of loop")

# for-else loop
 # if for loop doesn't get executed use else block to execute else condition

age=[22,23,25,21,26]
for age in age:
    if age<20:
        print("you are a teenager")
        break
else:
    print("no one is teenager\n") # output



# walrus operator(:=) assigning variable and writng expression a the same time
a=15
b=5
c=a%b
if(c):
    print("not divisible")

if(d:=a%b): # skip if block because d=0 and 0=false
    print(f"not divisible remainder exist {d}") 
print(d)# output 0