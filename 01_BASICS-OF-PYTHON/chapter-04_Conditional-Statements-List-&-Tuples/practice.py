 # 1. 
num = int(input("Enter a number: "))
if num > 0:
  print('Number is positive.')
elif num < 0 :
  print("Number is Negative.")
else :
  print('Number is Zero.')

# 2. 
foods = []
print("Enter 3 foods name")
food1 = input("food 1: ") 
foods.append(food1)
food2 = input("food 2: ") 
foods.append(food2)
food3 = input("food 3: ") 
foods.append(food3)
print(foods)
print(len(foods))

# 3. 
print("Enter your 3 favorite movies")
movie1 = input("Movie 1:")
movie2 = input("Movie 2:")
movie3 = input("Movie 3:")
movies = [movie1, movie2, movie3]
print(movies) 

# 4.
marksTuple = (87, 64,33,95,76)
print(f"Highest Marks: {max(marksTuple)}\nLowest Marks: {min(marksTuple)}")

# 5. 
marks = int(input("Enter your marks "))
if marks >= 90:
  print("Your grade is A.")
elif marks >=80:
  print("Your grade is B.")
elif  marks >=70:
  print("Your grade is C.")
elif  marks >=50:
  print("Your grade is D.")
elif marks >=36:
  print("Your grade is F.")
else:
  print("You are fail.")