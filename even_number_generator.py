def even_numbers(limit):
    for i in range(0 , limit+1 , 2):
        yield i

# get the upper limit from user input
try:
    user_limit =  int(input("Enter the limit from even numbers : "))
   
    # iterate over the generator and print the numbers
    print(f"Even number up to {user_limit}")
    for number in even_numbers(user_limit):
        print(number)


except ValueError:
    print("please enter a valid integer.")
