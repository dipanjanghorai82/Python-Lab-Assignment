def calculate_factorial(n):
    if n < 0:
        return "not defined for negative numbers." 
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

try:
    num = int(input("Enter an integer : "))
    result = calculate_factorial(num)
    print(f"the factorial is : {result}")
except ValueError:
    print("Invalid input ! please enter a valid input")