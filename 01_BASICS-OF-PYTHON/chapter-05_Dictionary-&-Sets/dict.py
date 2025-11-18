my_dict = {
  "name": "Khushboo",
  "age": 20,
  "city": "Jhunjhunu",
  "name": "Khushi"
}
print(type(my_dict))

my_dict["city"] = "Jaipur"

print(f"Name: {my_dict["name"]}")
print(f"Age: {my_dict["age"]}")
print(f"City: {my_dict["city"]}")

# Add a new pair ==>
my_dict["rollno."] = 21

# Delete existing key ==>
my_dict.pop("city")

# Check all keys ==>
print(my_dict.keys())

# Print all values ==>
print(my_dict.values())

# Create a copy ==>
copy = my_dict.copy()
# print(copy)

# print dict as tuple formate ==>
print(my_dict.items())


# clear the dictionary ==>
# my_dict.clear()