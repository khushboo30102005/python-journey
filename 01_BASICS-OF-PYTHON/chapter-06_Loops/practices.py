#  1. Write a Python program to print numbers from 1 to 10 using a while loop.
num = 1
while num<=10:
  print(num)
  num +=1
  
#2. Write a program to print numbers from 10 down to 1 using a while loop.
num = 10
while num>0:
  print(num)
  num -=1
  
# 3. Write a program to print all even numbers between 1 and 50 using a while loop.  
num = 1
while num<=50:
  if num%2==0 :
    print(num)
  num += 1
 
# 4. Write a program that prints the sum of first n natural numbers.
# For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15.

num = 1
n = 15
sum = 0
while(num<=n):
  sum += num
  num += 1
print(sum)  

#  5. Write a program to print this pattern using a while loop:
num = 1
while num<=15:
  print('*' * num)
  num +=1

# 6. Saumya wants to print her name 5 times, but each time with a number in front of it.

num = 1
while num<=5:
  print(f"{num}. Saumya Dii")
  num +=1

# 7. Write a program to print the multiplication table of any number using a while loop.

num = 1
while num<=10:
  print(30*num)
  num +=1
 
# FOR LOOP PRACTICES QUESTIONS:
 
# 8. Write a program using for and range() to print all even numbers between 1 and 20.
for e in range(1,21):
  if e%2==0:
    print(e)

# 9. Write a program to print numbers from 1 to 50, but print "Saumya Singh" instead of numbers that are multiples of 5.
  
for i in range(1,51):
  if i % 5 == 0:
    print("Saumya Singh")  
  else :
    print(i)  

# 9. Write a program to print numbers from 1 to 50, but print "Saumya Singh" instead of numbers that are multiples of 5.

for s  in range(1, 11):
  print(s**2)

# 11.Write a program that prints the multiplication table of any number entered by the user using a for loop.
num = int(input("Enter a number: "))
for m in range(1,11):
  print(f"{num} x {m} = {num*m}")

# 12.Write a program that prints all numbers from 100 to 1 using for and range().
for r in range(100, 0, -1):
  print(r)

# 13.Saumya wants to print her username five times in uppercase letters.
for i in range(1,6):
  print("SAUMYA1SINGH".upper())

# 14.You are given a list of Saumya’s favorite foods. Write a Python program to print each food item using a for loop.
foodList = ['GulabJamun', 'Chocolate', 'burger', 'Apple']
for food in foodList:
  print(food)

# 15.Saumya has created a tuple of countries she has already traveled to. Write a Python program to print each country using a for loop.
countries_traveled = ("Malaysia", "Vietnam", "Switzerland", "Italy", "Bhutan")
for country in countries_traveled:
  print(country)

# 4️⃣ break, continue, and pass 
# 17. Write a program that prints numbers 1 to 10, but skips the number 7 using the continue statement.

for i in range(1,11):
  if i == 7:
    continue
  print(i)

#18. Practice Question 4 Write a program using nested loops to print this pattern:

for i in range(1,2):
  for j in range(1,4):
    print('*'*(i*j))

# Practice Set (Quick Recap)
# 1. Print numbers from 1 to 100 using a for loop.
for i in range(1,101):
  print(i)

# 2. Print numbers from 100 to 1 using a while loop.
num = 100
while(num>0):
  print(num)
  num-=1

# 3. Print all numbers between 1 and 50 except multiples of 5.

for i in range(1,51):
  if i%5 == 0:
    continue
  print(i)

# 4. Create a program that asks the user for 5 favorite foods and prints them one by one.
food = []
num = 1
while num<=5:
  my_fav = input("Enter your favFood: ")
  food.append(my_fav)
  num += 1
  
print("Your favorite foods:")
for f in food:
    print(f)

# 5. Print the sum of first 10 natural numbers using a while loop.
num = 1
sum = 0
while num<=10:
  sum += num
  num += 1
print(sum)  