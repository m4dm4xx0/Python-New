#variable is a container for a value (string, integer, float, boolean)
#            a variable behaves as if it was the vale it contains

# Strings
first_name = "Lydia"
firstName = 'Lydia'
food = "pizza"
email = "lydia123@fake.com"
print(first_name)

# Integers
age = 25
quantity = 3
num_of_students = 30

#insert a variable in a print statement f-string
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#float
price = 10.99
gpa = 4.2
distance = 5.5

print(f"the price is ${price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance} km")

# Booleans

is_student = True

if(is_student):
    print("You are a student")
else:
    print("You're NOT a student")

for_sale = False

if for_sale:
    print("It is for sale")
else:
    print("It is NOT available")

is_online = True

if is_online:
    print("You are online")
else:
    print("You are offline")
