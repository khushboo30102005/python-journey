# Practice Questions

""" 1. Write a function named welcome_message() that prints “Welcome to
Python Programming!” three times. """

def welcome_message():
  print("Welcome to Python Programming!")
  
welcome_message() 
welcome_message() 
welcome_message() 

""" 2. Define a function inspire() that prints a motivational quote with your name. """

def inspire():
  print("Think OutSide The BOX.  -- Khushboo Saini")
  
inspire()  

""" 1. Write a function display_python() that prints "Python is Fun!". """

def display_python():
  print("Python is Fun!")
  
display_python()

""" 2. Create a function learn() that prints three Python topics. """  

def learn():
  print("1. DataTypes and Variables\n2. Loops\n3. Functions")
learn()  

""" 1. Write a function show_age(name, age) that prints: "Saumya Singh is 21 years old." """
def show_age(name = "Khushboo", age = 21):
  print(f"{name} is {age} years old.")

show_age("Saumya Singh", 21)  
show_age()

""" 2. Create a function add_numbers(a, b) that prints both the sum and
difference. """

def add_numbers(a, b):
  print(f"{a} + {b} = {a+b}")
  print(f"{a} - {b} = {a-b}")
add_numbers(6, 3)  

""" 3. Write a function fav_food(food) that prints "Saumya loves <food>". """

def fav_food(food):
  print(f"Saumya loves {food}.")

fav_food("Samosa")

""" 1. Write a function square(num) that returns the square of a number. """

def square(num = 10):
  return num**2

print(square(53))

""" 2. Write a function that takes a string and returns the count of vowels and consonants separately. """

def countOfVowelConsonants(str):
  str = str.lower()
  vowel = "aeiou"
  vowelCount = 0
  consonants = 0
  for i in str:
    if i.isalpha():
      if i in vowel:
        vowelCount+=1
      else:
        consonants+=1
  return {"vowel": vowelCount, "consonants": consonants}      

print(countOfVowelConsonants("KHUSHBOO saini"))

""" 3. Define a function convert_to_upper(word) that returns the uppercase
version of the string. """

def convert_to_upper(word):
  return word.upper()

print(convert_to_upper("learn python with saumya dii.") ) 

""" 4. Create a function full_name(fname, lname) that returns the full name
joined with a space. """

def full_name(fname, lname):
  return fname+' '+lname

print(full_name("Khushboo", "Saini"))

""" 1. Define a function message(text="Keep Learning!") and call it with and
without an argument. """

def message(text="Keep Learning!"):
  return text
print(message())

""" 2. Create a function login(username, password="1234") that prints the
credentials. """

def login(username, password="1234"):
  return {"userName": username, "Password": password}

print(login("Khushboo saini"))

""" 1. Write a program with a local variable score inside a function and a global
one outside. """

x = 5
def var():
  y = 10
  return {"global variable": x, "local variable": y}

print(var())

""" 2. Create a program using global keyword to modify a variable from inside
a function. """

a = "A"
def modifyVar():
  a = 1
  return a
print(modifyVar())