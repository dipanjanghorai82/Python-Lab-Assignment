import re
user_input = input("enter a sentence with number : ")
pattern = r"^\d+"
replacement = "XX"

modified_string = re.sub(pattern , replacement , user_input)

print("original text : " , user_input)
print("modified string : " , modified_string)

