# Laat python 2 getallen optellen en het resultaat printen
#  5 + 3 = 8

getal1 = 5
getal2 = 3
resultaat = getal1 + getal2
print(resultaat)

# Laat python 2 getallen vermenigvuldigen en het resultaat printen
#  3 * 4 = 12
getal2 = 3
getal3 = 4
resultaat = getal2 * getal3
print(resultaat)

# Geef nu het resultaat weer in een string. waar de getallen en het resultaat in staan.
print(f"{getal2} * {getal3} = {resultaat}")

### Laat python de wortel van een getal berekenen en het resultaat printen
## De wortel van 16 is 4
# Tip gebruik ** om de wortel te berekenen
getal4 = 16
wortel = getal4 ** 0.5
print(f"De wortel van {getal4} is {wortel}")

### Laat python de rest van een deling berekenen en het resultaat printen
#  De rest van 10 / 3 is 1
getal5 = 10
getal6 = 3
rest = getal5 % getal6
print(f"De rest van {getal5} / {getal6} is {rest}")

### Maak een calculator die 2 getallen optelt, aftrekt, vermenigvuldigd en deelt
## Gebruik hiervoor input om de getallen te vragen
# Voer getal 1 in: 5
# Voer getal 2 in: 3
# 5 + 3 = 8
# 5 - 3 = 2
# 5 * 3 = 15
# 5 / 3 = 1.6666666666666667

getal7 = int(input("Voer getal 1 in: "))
getal8 = int(input("Voer getal 2 in: "))
resultaat = getal7 + getal8
print(f"{getal7} + {getal8} = {resultaat}")
resultaat = getal7 - getal8
print(f"{getal7} - {getal8} = {resultaat}")
resultaat = getal7 * getal8
print(f"{getal7} * {getal8} = {resultaat}")
resultaat = getal7 / getal8
print(f"{getal7} / {getal8} = {resultaat}")