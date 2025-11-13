# Syntax 

str1 = 'hello World'
str2 = "Hello Python"
str3 = '''Python course by Saumya dii'''
print(str1)
print(str2)
print(str3)

# Strings Concatenation 
print("hello" + " Strings")     # Output ==> hello Strings

# Length of string

print(len("Khushboo"))          # Output ==> 8

# Indexing ==>
str = "Samosa"
print(str[0])       # Output ==>  S


#  Strings are immutable ==>

# str[0] = 'H'    #  TypeError: 'str' object does not support item assignment

# Slicing ==>  str[start:end]  end index is excluded
print(str2[:])     #Hello Python
print(str2[:5])     #Hello
print(str2[:5])     #Hello
print(str2[6:])     #Python

# Negative Indexing ==>  (...-3,-2,-1)
str = "Samosa"
print(str[-1])       # Output ==>  a 

# STRING METHODS:
str = "Khushboo saini"
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print(str.find("oo"))
print(str.replace("saini", "best"))
print(str.count("o"))

# formatted strings (f-strings)
name = "Khushboo saini"
age =19
print(f"My name is {name} and i'm {age} years old.")

# Escape sequence
print('hello\nworld')
print('hello\tworld')
print('hello\\world')
print('hello\'world')
print("hello\"world")

#  Repetition :
print("YUM!!" * 3)

# Membership  :
print("a" in "banana")
print("f" not in "banana")