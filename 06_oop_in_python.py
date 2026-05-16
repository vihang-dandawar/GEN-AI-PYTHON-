class Chai:
    pass

class Coffee:
    pass

masalaChai=Chai() # obj of Chai class
coldCoffee=Coffee()
print(masalaChai)
print(Chai.__name__)
print(coldCoffee is Chai)# false

# obj can access properties of class if they modify class properties by default changes will not reflect in class but for that resp obj

# adding properties to class
Chai.is_hot=True
Chai.milk="Amul"


print(masalaChai.milk) # amul because we just add these properties to class

masalaChai.milk="Gokul" # obj property changes doesn't affect  properties at class level
print(f"masala chai milk (obj) {masalaChai.milk}")
print(f"Chai class milk (class) {Chai.milk}")

# Note if you delete properties from  obj then the property  will set to value defined in class

del masalaChai.milk
print(masalaChai.milk) # set to gokul but after delete milk gets value set in class=amul

#--------------------------------------------------------------


# self args
class Chaicup:
    size=150 #ml

    def describe(self):# in this func you can access any properties from class
        return f" size  of cup is {self.size} ml "


cup=Chaicup()
print(cup.describe()) 
cup.size=100 #ml
print(Chaicup.describe(cup)) #  context is provided just like self


# we can  create constructor in python via __init__
class Chaiorder:
    def __init__(self,type_,size):
        self.type=type_
        self.size=size
    
    def summary(self):
        return f" type of chai is {self.type} & size of cup is {self.size}"
    

# created an instance of class
order1=Chaiorder("masala chai",150) # passed args mentioned in constructor(__init__)
print(order1.summary())

#------------------------------------------------------

# Inheritence 
class Super:
    def __init__(self,type_): # type_var name and type is built in for type checking
        self.type=type_
        
    def prepare(self):
        return f"preparing {self.type}...."

class Base(Super): # super class inherited base class
    def add_spices(self):
        print("Adding cardoman,ginger....")
    def __init__(self, type_):
        super().__init__(type_)# calling super class constructor 


# Composition is an object-oriented design principle where one class contains objects of other classes in order to use their functionality.
class chaiShop:
    chai_cls=Base # holding  a class (not obj because () parenthesis is not there)

    def __init__(self):
        self.chai=self.chai_cls("Masala chai")

    def serve(self):
        print(f"serving {self.chai.type} in the shop")
        print(self.chai.prepare())
chaiShop1=chaiShop()
chaiShop1.serve()


# Method Resolution Order(MRO )
class A:
    label="A is calling"

class B(A):
    label="B is calling"

class C(A):
    label= "C is calling"

class D(B,C):
    pass

#        A
#       /\
#      B  C   B extend A,C extend A
#      \ /
#       D        D extends B,C

# if i call label from D which will be execute ?

d1=D()
print(d1.label)
# D first extends B and then C so B's label will be executed,
# order of inheritance matters
# to check the order use dunder mro
print(D.__mro__,"\n\n")
#(<class '__main__.D'>,
#  <class '__main__.B'>, <class '__main__.C'>,
#  <class '__main__.A'>, <class 'object'>)


#------------------------------------------------------------------


# static function
# these are the methods which doesnt require obj creation for execution

class Chai:
    @staticmethod
    def cleanWords(text):
         return [ word.strip() for word in text.split(",")]

text="Hey, im, vihang   ,dandawar   , and, i, want ,a, job,"    
wordArr=Chai.cleanWords(text)
print(wordArr)
#---------------------------------------------------

class ChaiOrders:
    def __init__(self,type_,sweetness,size):
        self.type=type_
        self.sweetness=sweetness
        self.size=size

    @classmethod
    def getfrom_Dict(cls,order_data):
        return cls(
            order_data["type"],
            order_data["sweetness"],
            order_data["size"]
        )
    # it gives different ways to create obj 
   # Instead of writing long logic in __init__, you can define alternate constructors:
    @classmethod  # cls is class ,we are passing directly class here
    def getFrom_string(cls,order_string):
        type,sweetness,size=order_string.split(",")
        return cls(type,sweetness,size)
    
    def __repr__(self):
        return f"ChaiOrders(type={self.type}, sweetness={self.sweetness}, size={self.size})"


order1=ChaiOrders.getFrom_string("masalaChai,low,150ml")
print(order1)

order2=ChaiOrders.getfrom_Dict({"type":"ilaichi chai","sweetness":"medium","size":"low"})
print(order2)

# property decorator
# setter and getter
class Chai:
    def __init__(self, type_):
        self._type = type_   # notice underscore(_type) → "private" by convention(means type is private property it needs getter & setter)

    @property
    def type(self):   # getter
        print("Getting type...")
        return self._type

    @type.setter
    def type(self, value):   # setter
        print("Setting type...")
        if not value.endswith("Chai"):
            raise ValueError("Type must end with 'Chai'")
        self._type = value

    @type.deleter
    def type(self):   # deleter (optional)
        print("Deleting type...")
        del self._type


chai = Chai("MasalaChai")
print(chai.type)       # calls getter
chai.type = "GingerChai"   # calls setter
del chai.type          # calls deleter
