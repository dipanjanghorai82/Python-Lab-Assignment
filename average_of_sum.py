# initialize an empty list to store the integers
numbers = []
# take 10 integers as input from the users
print("enter 10 integers : ")
for i in range(10):
    user_input = int(input(f"enter integers{i+1} : "))
    numbers.append(user_input)

# find the sum manually without using sum()
total_sum = 0
for num in numbers:
    total_sum += num

# len() is used to here get the total count of items in the list
avg = total_sum / len(numbers)

## display the result
print(f"\nthe list of numbers : {numbers}")
print(f"sum : {total_sum}")
print(f"average : {avg}")

      
