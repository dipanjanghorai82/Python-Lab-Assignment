smallest = None
largest = None

print("Enter 7 integer : ")

for i in range(1 , 8):
    num = int(input(f"Enter integer{i} : "))

    if smallest is None and largest is None:
        smallest = num
        largest = num
    else:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

print("\n____result_____") 
print(f"smallest integer : {smallest}")
print(f"largest integer : {largest}")
