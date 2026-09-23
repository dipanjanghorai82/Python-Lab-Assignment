numbers = list(map(int , input("enter integer seperated by space : ").split()))

# remove duplicates
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("list after removing duplicatesb : " , unique)
        
