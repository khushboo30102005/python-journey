year = 2025
month="November"
Wind_speed=1.92
is_winter=True

print("year: ", year, "  type: ",type(year) )
print("month: ", month, "  type: ",type(month) )
print("Wind_speed: ", Wind_speed, "  type: ",type(Wind_speed) )
print("is_winter: ", is_winter, "  type: ",type(is_winter) )

#  practice Question:
# 1 .  print datatype 
age = input("enter your age ")
print("age: ", age, "dataType is: ", type(age))

# 2. take two num and print sum and avg

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
sum=num1+num2
print("sum of", num1, "&", num2, "is:",sum)
print("Average is: ", sum/2)

# 3. take num as input convert it into float and print both original and converted value with their dataType

num = input("Enter a number: ")
floated_num = float(num)
print("Original number: ", num, "and its DataType: ", type(num))
print("Converted number: ", floated_num, "and its DataType: ", type(floated_num))