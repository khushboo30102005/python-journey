#  1.  take user's name as input and print: 1st char, last char, length
name = input("Enter user name: ")
print(name[0])
print(name[len(name)-1])
print(len(name))

# 2. 
favColor = 'GREEN'
length = len(favColor)
halfLength = length//2
print(favColor[halfLength-1:halfLength+2])
print(favColor[length-2:length])

# 3. 
statement = input("enter a statement: ")  

print(statement.upper())
print(statement.lower())
print(statement.replace(" ", "_"))

# Emoji converter :
msg = input("Enter your massage: ")
msg = msg.replace(":(", "☹️")
msg = msg.replace(":D", "😀")
msg = msg.replace(":)", "😊")
msg = msg.replace(";", "😎")
msg = msg.replace(".", "🤗")
print(msg)