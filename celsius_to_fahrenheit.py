def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


user_input = input("Enter temperature in Celsius: ")
c_temp = float(user_input)


f_temp = celsius_to_fahrenheit(c_temp)
print(f"{c_temp}°C is equal to {f_temp}°F")