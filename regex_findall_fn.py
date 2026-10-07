import re
pattern = r"^\d+"
user_string = input("enter a sentence with multiple numbers : ")
all_matches = re.findall(pattern , user_string)

if all_matches:
    print(f"marches found ! here is the list of all numbers : '{all_matches}'")
    print(f"total number found : '{all_matches}'")
else:
    print("no matches found")
    
        