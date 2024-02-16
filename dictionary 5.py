conversion_factors = {
    'Celsius': ('Fahrenheit', 1.8, 32),
    'Fahrenheit': ('Celsius', 0.5556, -32)
}

while True:
    print("\nTemperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * conversion_factors['Celsius'][1]) + conversion_factors['Celsius'][2]
        print(f"{celsius:.1f}°C is equal to {fahrenheit:.1f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - conversion_factors['Fahrenheit'][2]) * conversion_factors['Fahrenheit'][1]
        print(f"{fahrenheit:.1f}°F is equal to {celsius:.1f}°C")
    elif choice == "0":
        print("Exiting. Bye")
        break
    else:
        print("Invalid choice.")