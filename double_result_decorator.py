def double_result(func):
    def wrapper(*args , **kwargs):
        result = func(*args , **kwargs)
        return result * 2
    return wrapper

@double_result
def add(a , b):
    return a + b

try:
    num1 = float(input("Enter the first number(a) : "))
    num2 = float(input("Enter the second number(b) : "))

    # call the decorated function
    output = add(num1 , num2)
    print(f"Double result : {output}")

except ValueError:
    print("please enter a valid numeric values")
