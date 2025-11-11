# 1. Smart temp converter
# take input in celsius and print equivalent in fahrenheit and kelvin 

temp = int(input("Enter temperature in celsius: ")) 
fahrenheit_temp = (temp * 9/5) +32
kelvin_temp = temp + 273.15
print("TEMPERATURE IN CELSIUS IS :", temp,"deg C")
print("FAHRENHEIT IN CELSIUS IS :", fahrenheit_temp,"deg F")
print("KELVIN IN CELSIUS IS :", kelvin_temp,"K")

# 2. Bill split calculator ==>
total_bill = float(input("enter total bill amount: "))
friend_count = int(input("Enter number of friends: "))
splitted_bill= total_bill/friend_count
print("Total bill is", total_bill, "number of friends is", friend_count, ", so each person pay :", splitted_bill)


# 3. Predict the output 
x = 5
y = 2.0
print(x // y)   # 2
print(x ** y)  # 25

# 4. Identify the correct error ==>
# if = 10
# print(if)  #  invalid syntax , if is a keyword