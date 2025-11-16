""" # Conditional Statements ==>

marks = 29
if marks >= 90:
  print("Your grade is A.")
elif marks >=80:
  print("Your grade is B.")
elif  marks >=70:
  print("Your grade is C.")
elif  marks >=60:
  print("Your grade is D.")
elif marks >=36:
  print("Your grade is F.")
else:
  print("You are fail.")
  
#  Lists in Python ==>

subjects = ["React", "Python", "Redux", "DSA", "JavaScript",98]
print(subjects)
print(len(subjects))
  
# Methods in list ==>

# Lists are mutable ==>
subjects[0] = "Frontend" 
print(subjects) 

# List slicing ==>
print(subjects[0:2])

# max and min 
marks = [78,98,88,98,59]
print(f"Max:{max(marks)}")
print(f"Min:{min(marks)}")

# append
marks.append(76)
print(marks)

# insert
marks.insert(2, 33)
print(marks)

# remove
marks.remove(98)
print(marks)

# pop
marks.pop(1)
print(marks)

# sort
marks.sort()
print(marks)

# reverse
marks.reverse()
print(marks) """
 

#  Tuple in Python ==>  tuples are immutable
# Representation ==>
tuple = (43,45,34,87,43,69,99)

print(tuple[0])

# tuple[1] = 32      #TypeError: 'tuple' object does not support item assignment 

empty_tuple = ()
print(type(empty_tuple))
single_tuple = (3)
print(type(single_tuple) )
single_tuple = (3,)
print(type(single_tuple) )
print(tuple.index(87))
print(tuple.count(43))

fruitsTuple = ("Grapes", "Mango", "Apple", "WaterMelon")
print(len(fruitsTuple))
print(fruitsTuple[3])