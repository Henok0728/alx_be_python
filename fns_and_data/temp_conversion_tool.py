FAHRENHEIT_TO_CELSIUS_FACTOR = float(5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = float(9/5)
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def main():
    print("Temperature Conversion Tool")
    choice = input("Convert to (C)elsius or (F)ahrenheit? ").strip().upper()
    if choice == 'C':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = convert_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
    elif choice == 'F':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = convert_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    else:
        print("Invalid choice. Please select 'C' or 'F'.")
if __name__ == "__main__":
    main()
