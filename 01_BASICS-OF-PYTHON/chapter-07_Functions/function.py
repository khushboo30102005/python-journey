def sum(a=4,b=8):
  return a+b

addition = sum(12,4)
print(addition)


print(sum()) 

# keyword argument

def full_name(fname, lname):
  return fname+' '+lname

print(full_name(lname = "Saini", fname = "Khushboo"))

def sayHii():
  print("Hello Python")
  
print(sayHii())   # Return ==> None