# ## take input from the users
# user_input = input("Enter elements seperatd by space : ")
# my_list = user_input.split()

# ## set up two pointers

# left = 0
# right = len(my_list) - 1

# ## swap two elements until the pointers meet in the middle
# while left < right:
#     my_list[left] , my_list[right] = my_list[right] , my_list[left]
#     left += 1
#     right += 1

# print(f"Reverse list (in-place) : " , my_list)


items = input("enter items seperated by space : ").split()

reverse_item = []

## loop through the items backwards
for i in items:
    reverse_item.insert(0 , i)

print("reverse list : " , reverse_item)
