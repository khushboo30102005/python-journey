languages = {"JavaScript", "Python", "Java", "C", "Java"}
# print(type(languages))
languages.add("C++")
languages.remove("Java")
print(languages)  
languages.pop()
print(languages)    
emptySet = set()
print(type(emptySet))

# Union & InterSection 

subjects = {"AI/ML", "Computer Networks", "DSA", "Python"}

print(subjects.union(languages))
print(subjects.intersection(languages))