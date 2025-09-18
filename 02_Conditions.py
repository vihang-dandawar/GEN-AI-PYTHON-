# order=input("Enter your order:")
# if order=="samosa" or order=="kachori":
#     print(f"wait 5 min your {order} is being ready")
# else:
#     print(f"Order somrthing else we dont serve {order}")

    # elif for nested if conditions
    # pass: pass is a placeholder that does nothing and allows 
    # execution to continue normally within the current code block.

a =20
if a <20:
    print("a <20")
else:
    pass   # does nothing 
    print("a=20") 

order_amount=int(input("Enter order amount"))
delivery_fees= 30 if order_amount>300 else 0 # if-else in single line ternary operator-> ?: in java
print(f"Delivery fees for order amount  {order_amount} is {delivery_fees}")
       
# switch case in python 

seat_type=input("Enter seat type :")
match seat_type:
    case "sleeper":
        print(f"your seat is {seat_type} beware fo thieves")
    case "AC":
        print("your seat is {seat_type} you get free meal")
    case _:
        print("Invalid seat")  # default case