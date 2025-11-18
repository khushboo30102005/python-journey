# 1. dictionary : meaning of 3 english words
englishDict = {
  "Kudos": "Praise or honor",
  "Lethargic": "Sluggish or inactive",
  "Meticulous": "Showing great attention to detail",
}
print(englishDict)

#2. set : Union and InterSection
A = {1,2,3,4,5}
B = {5,4,3,8,7}
A_union_B = A.union(B)
A_intersection_B = A.intersection(B)
print(f"Union: {A_union_B}")
print(f"InterSection: {A_intersection_B}")

# 3. Try to add both integer 9 and float 9.0 to a set and observe what happens.
set = {9, "9.0"}  
print(set)