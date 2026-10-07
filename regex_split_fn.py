import re
user_input = input("enter items separated by commas , semicolons , or spaces : ")
pattern = r"[;,\s]+"
split_list = re.split(pattern , user_input)
print("original text : ", user_input)
print("split List : " ,split_list)
