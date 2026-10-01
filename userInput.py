# input() = A function that prompts the user to enter data
#           Return the entered data as a string

name = input("What is your name?: ")
age = input ("How old are you?: ") # ALWAYS A STRING

#or age = int(input ("How old are you?: ") # ALWAYS A STRING)

age = int(age)
age+=1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old") 

# Calculate the are area of a rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area is: {area} cm²") #shift + alt +0178

#Shopping Cart Program
item = input("Waht item would you like to buy?: ")
price = float(input("What is the price ? "))
quantity = int(input("How many would you like? "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s for ${total}")
