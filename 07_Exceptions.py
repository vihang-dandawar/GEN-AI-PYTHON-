chai_menu={"milk":30,"tea":40}
try:
     coffee=chai_menu["coffee"]
     print(f"{coffee} found")
except:
    print("key doesnt exist in dictionary")
finally:
    print("finally  block always exists")

    # keyerror : key doesnt exist in dict
    # type error 15*three
    # valueError value doesn't exist
#--------------------------------------------------------------

    # raise your own excp
def make_Chai(flavour):
    if flavour not in ["masala chai","ilaichi chai","ginger chai"]:
        raise ValueError("unsupported chai flavour...")
    
# make_Chai("mint") # excp occured


#-----------------------------------------------------------

# Raise your own Exception
class OutofIngredientException(Exception): # extends excp class
    pass

def makeChai(milk,sugar):
    if milk==0 or sugar==0:
        raise OutofIngredientException("Missing Milk or Sugar")
    print("chai is ready...")

makeChai(1,0)

#-----------------------------------------------------
# File Handling
f= open("order.txt","w")
try:
    f.write("Writing something in the file")
except:
    f.close() #  open -> we have to explicitely close the file
#If you forget to call f.close(), the file may stay open → memory leaks, data not saved properly.

# w-> write,r-> read

with open("example.txt","w") as f1:
    f1.write("Again writing something in the file")
    # with keyword->  automatically closes the file when the block ends, even if an error happens