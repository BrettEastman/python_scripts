name = "Brett"
age = 44

f_string = f"My name is {name} and I am {age} years old."
string_formatting = "My name is {} and I am {} years old."

print(f_string)
print(string_formatting.format(name, age))

print("Hi {}, you are {}".format(name, age))
print("Hi {name}, you are {age}".format(name=name, age=age))
