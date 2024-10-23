def ubah_temperature(value, unit):
    if unit == 'C':
        # Ubah Celsius to Fahrenheit
        fahrenheit = (value * 9/5) + 32
        return f"{value}°C adalah {fahrenheit:.2f}°F"
    elif unit == 'F':
        # Ubah Fahrenheit to Celsius
        celsius = (value - 32) * 5/9
        return f"{value}°F adalah {celsius:.2f}°C"
    else:
        return "Tidak Valid! Pakai 'C' untuk Celsius atau 'F' untuk Fahrenheit."


temperature = float(input("Masukkan Nilai Temperature: "))
unit = input("Masukkan Unit Temperature ('C' untuk Celsius, 'F' untuk Fahrenheit): ").upper()

print(ubah_temperature(temperature, unit))