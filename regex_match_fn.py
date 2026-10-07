import re

pattern = r"^(Hello|Hi)"

user_string = input("Enter a sentence : ")

match_result = re.match(pattern , user_string)

if match_result:
    print(f"match found at the start ! your sentence begins with  : '{match_result.group()}'")
else:
    print(f"no match ! the sentence does not start with 'Hello' or 'Hi' . " )    