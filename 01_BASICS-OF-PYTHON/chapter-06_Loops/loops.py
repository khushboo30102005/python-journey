# while loop ==>

# print name 100 times
print("hii")
num = 1
while (num<=10):
  print( "Khushboo")
  num += 1
  
# for loop ==>

# A for loop is used to iterate sequences like lists, tuples, and strings

food = ["cake", 'chocolate', 'burger'] 
for i in food:
  print(i)   
  
  
# for Loop with range()
for i in range(1,5,1):
  print(i)
  
for item in range(2,21,2):
  print(item)  

# 5️⃣Nested Loops ==>
for i in range(1,5):
   for j in range(1,5):
     print( i, j )
