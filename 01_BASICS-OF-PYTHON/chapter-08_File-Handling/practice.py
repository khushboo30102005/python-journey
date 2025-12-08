""" 1. Write code to open a file named mydata.txt in read mode. """
# open("mydata.txt", 'r')

""" 2. Write a program to read a text from a given file certificate.txt and find whether it contains the word live. """

# file = open("certificate.txt", 'r')

# data = file.read()
# data = data.lower()
# if 'live' in data:
#   print("YES")
# else:
#   print("NO")  
# print(data.__contains__('live'))

""" 3. What happens if you open a non-existing file in "r" mode? """
# file = open("certificate2.txt", 'r')  # ERROR ==> FileNotFoundError

""" 4. Open a file called report.txt in write mode. """
# reportFile = open("report.txt", 'a')
# reportFile.write("Hello PYTHON \n")

""" 4. Create a file named saumya_info.txt using "x" mode. """
# open("saumya_info.txt", 'x')   # Error if File Already Exist: FileExistsError

""" 5. Write a program to safely check whether a file exists before opening it. """
# try:
#   open("Khushboo_info.txt", 'x')
# except FileExistsError as e:
#   print("Error", e)  

""" 1. Read a file named story.txt and print the full content. """
# with open("story.txt", 'r') as f:
#   fileData = f.read()
#   print("fileData:\n", fileData)
  
""" 2. Read only the first line of story.txt. """
# with open("story.txt", 'r') as f:
#   line1 = f.readline()
#   print("line1:", line1)

""" 3. Print how many lines are present in story.txt. """
# with open("story.txt", 'r') as f:
#   dataList = f.readlines()
#   print(len(dataList))
  
""" 1. Write your name and class into a file named khushboo_info.txt. """  
# with open("Khushboo_info.txt", 'w') as f:
#   f.write("Name: Khushboo saini")
#   f.write("\nClass: MCA 2nd SEM")

""" 2. Create a file khushboo_info.txt and write 3 goals for this month. """
# with open("khushboo_info.txt", 'a') as f:
#   f.write("\nGOALS FOR THIS MONTH:")
#   f.write("\nComplete React and Redux.")
#   f.write("\nExplore TypeScript.")
#   f.write("\nBuild Snack Game in JavaScript.")
  
""" 1. Copy khushboo_info.txt to mydata.txt. """  
# import shutil
# shutil.copy("khushboo_info.txt", "mydata.txt")

""" 2. Rename saumya_info.txt to Intro.txt. """
# import os
# os.rename("saumya_info.txt", "Intro.txt")

""" 3. Ask user for a filename and copy it to a backup folder. """
# import shutil
# userFile = input("Enter your file name for backup: ")
# shutil.copy(userFile, f"{userFile}-backup.txt")

""" 8️⃣Real-Life Mini Example: Saumya’s Daily Log App """
# import datetime
# with open("mylog.txt", "a") as f:
#   f.write(f"Saumya logged in at {datetime.datetime.now()}\n")
 