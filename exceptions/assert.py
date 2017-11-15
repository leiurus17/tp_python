def kelvin_to_fahrenheit(temp):
    assert (temp >= 0), "Colder than absolute zero!"
    return ((temp - 273) * 1.8) + 32

print kelvin_to_fahrenheit(273)
print int(kelvin_to_fahrenheit(505.78))
print kelvin_to_fahrenheit(-5)