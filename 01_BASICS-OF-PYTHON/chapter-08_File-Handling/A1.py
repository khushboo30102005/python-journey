# file = open("file-Handling.txt", 'w')
# file.write("Learning Python With Saumya singh.\n")

# file.write("Cover almost all basics. and also make some projects")
# file.close()

# file = open("file-Handling.txt", 'r')
# data = file.read()
# print(data)
# file.close()


# with keyword ==>

# with open("file-Handling.txt", 'r') as f:
#   fileData = f.read()
#   print(fileData)


# Read Line by line ==>

with open("file-Handling.txt",'r') as f:
  line1 = f.readline()
  line2 = f.readline()
  line3 = f.readlines()
  print(f"Line1: {line1}Line2: {line2}\nLine3:{line3}")
  fileData = f.read()
  print("fileData",fileData)
  
# Read Lines==>  List all line  

with open("file-Handling.txt",'r') as f:
  line3 = f.readlines()
  print(f"\nLine3:{line3}")  