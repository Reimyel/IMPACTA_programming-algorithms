def converter_celsius(c):
    f = (float(c) * 1.8) + 32
    return f

celsiusInput = input("Digite o a temperatura em Celsius: ")

print(f"A temperatura em Fahrenheit é {converter_celsius(celsiusInput):.2f}")