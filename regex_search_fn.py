import re
pattern = r"\d+"
user_string = input("enter a string : ")

match_result = re.match(pattern , user_string)

if match_result:
    print(f"match found ! the first number in your text is : '{match_result.group()}'")
else:
    print("no match found ! there are no numbers in your string") 
       