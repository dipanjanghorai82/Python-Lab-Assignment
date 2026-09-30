def show_info(func):
    def wrapper(*args , **kwargs):
        print("calling functions.....")
        result = func(*args , **kwargs)
        print("function executed.....")
        return result
    return wrapper

@show_info
def square(num):
    return num * num

try:
    user_num = float(input("Enter a number to square : "))

    # call the decorated function
    output = square(user_num)
    print(f"Result : {output}")

except ValueError:
    print("please enter a valid numeric value.")
    
