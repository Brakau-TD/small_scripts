import sys

ABSOLUTER_NP_C = -273.15
k = 1


def get_float(msg="Bitte Zahl eingeben: "):
    while True:
        try:
            f = float(input(msg))
            return f
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")


def celsius_kelvin(num):
    kelvin = num + abs(ABSOLUTER_NP_C)
    print(str(kelvin) + 'K')


def celsius_fahrenheit(num):
    fahrenheit = num*1.8 + 32
    print(str(fahrenheit) + '°F')


def kelvin_celsius(num):
    celsius = num + ABSOLUTER_NP_C
    print(str(celsius) + '°C')


def kelvin_fahrenheit(num):
    fahrenheit = (num + ABSOLUTER_NP_C)*1.8 + 32
    print(str(fahrenheit) + '°F')


def fahrenheit_celsius(num):
    celsius = (num - 32)/1.8
    print(str(celsius) + '°C')


def fahrenheit_kelvin(num):
    kelvin = (num - 32)/1.8 + abs(ABSOLUTER_NP_C)
    print(str(kelvin) + 'K')


print("Gib 'ck' ein, um Celsius in Kelvin umzurechnen, 'cf' für Celsius nach Fahrenheit, 'kc' für Kelvin"
      " nach Celsius, 'kf' für Kelvin nach Fahrenheit, 'fc' für Fahrenheit nach Celsius und 'fk' für Fahrenheit"
      "nach Kelvin\nDrücke Enter, um das Programm zu beenden.")

while k == 1:
    c = input()
    if str.lower(c) == 'ck':
        celsius_kelvin(get_float())
        k = 0
    elif str.lower(c) == 'cf':
        celsius_fahrenheit(get_float())
        k = 0
    elif str.lower(c) == 'kc':
        kelvin_celsius(get_float())
        k = 0
    elif str.lower(c) == 'kf':
        kelvin_fahrenheit(get_float())
        k = 0
    elif str.lower(c) == 'fc':
        fahrenheit_celsius(get_float())
        k = 0
    elif str.lower(c) == 'fk':
        fahrenheit_kelvin(get_float())
        k = 0
    elif c == '':
        sys.exit()
    else:
        print('Gib eine gültige Eingabe ein!')
        continue