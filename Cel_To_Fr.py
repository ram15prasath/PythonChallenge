def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius_input = float(input("Enter temperature in Celsius: "))

fahrenheit_output = celsius_to_fahrenheit(celsius_input)
print(f"The temperature in Fahrenheit is: {fahrenheit_output}")