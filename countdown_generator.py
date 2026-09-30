def coundown(n):
    while n >= 1:
        yield n
        n -= 1

# get start number from user input
try:
    user_input = int(input("Enter a number to start the coundown fromm :"))
    # iterate over the generator and print the numbers
    
    for number in coundown(user_input):
        print(number)

except ValueError:
    print("please enter a valid integer")

