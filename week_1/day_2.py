# COMMENTS

# This is a single line comment use for documentations.

'''
This is a multiline comment.
You can see me write text in a new line.
This is use for documentations.
'''


# Variables & Data-types: a simople container that holds a value
bottle = "water"

#Data Types: specifically of characters
"Friends" # String

122345667 # Integers

1233.5876 # Floats

True
False # Boolean


first_name = "Miracle" # Snake case



world = "Hello World!"
# print(world)

# Arithmetic Operators
'''
+ Addition (Datatypes - Inetgers, Floats, Strings)
- Subtraction (Datatypes - Inetgers, Floats, Strings)
* Multiplication (Datatypes - Inetgers, Floats, Strings)
/ Division (Datatypes - Inetgers, Floats)
// Floor Division (For rounding down values) (Datatypes - Inetgers, Floats)
'''

addition = 12 + 12 # Addition
concatenation = "Miracle" + "King" # Concatenation
repitition = "Hurray" * 3 # Repitition

print(concatenation)
print(addition)
print(repitition)



first_number = 4 
second_number = 6

# Addition
add = first_number + second_number
print("Addition:", add, "Type:", type(add))

# Substraction
subsctract = first_number - second_number
print("Subsctraction:", subsctract, "Type:", type(subsctract))

# Division
divide = first_number / second_number
print("Division:", divide, "Type:", type(divide))

# Multiplication 
multiply = first_number * second_number
print("Muplication:", multiply, "Type:", type(multiply))



# Casting - Changing one data type to another data type
'''
int() - to convert to integer (string, float)
str() - ... string (integer, boolean, float)
float() - ... float (integer, boolean, float)
bool() - ... boolean ("string")
'''

# Converting divide to an integer
convert_to_int = int(divide)
print("converting divide to integer:", convert_to_int, type(convert_to_int))

convert_to_int = int(add) 
print("converting addition to integer:", convert_to_int, type(convert_to_int))

convert_to_int = int(multiply)
print("converting division to integer:", convert_to_int, type(convert_to_int) )

convert_to_int = int(subsctract)
print("converting substraction to integer:", convert_to_int, type(convert_to_int))


# Re-assigning a variable
nationality = "United State of America"
nationality = "Nigeria"
nationality = "France"

introduction = "My name is" + " " + first_name + " " + "and I am from" +  " "+ nationality
print(introduction)
