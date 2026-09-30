items = input("enter items seperated by space : ").split()

reverse_item = []

## loop through the items backwards
for i in items:
    reverse_item.insert(0 , i)

print("reverse list : " , reverse_item)
