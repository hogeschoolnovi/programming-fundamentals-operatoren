# geef 2 getallen op en kijk of ze gelijk zijn
# 5 en 5 zijn gelijk
# 5 en 3 zijn niet gelijk

getal1 = 5
getal2 = 5
getal3 = 3
print(f"zijn {getal1} en {getal2} gelijk? :  {getal2 == getal1}")
print(f"zijn {getal1} en {getal3} gelijk? :  {getal3 == getal1}")

# geef 2 getallen op en kijk of getal1 groter is dan getal2
# 5 is groter dan 3
# 3 is niet groter dan 5
print(f"{getal1} is groter dan {getal3} : {getal1 > getal3}")
print(f"{getal3} is groter dan {getal1} : {getal3 > getal1}")


# geef 2 getallen op en kijk of getal1 kleiner is dan getal2 of gelijk aan getal2
# 5 is kleiner dan 3
# 3 is kleiner dan 5
# 5 is niet kleiner dan 5
print(f"{getal1} is kleiner dan of gelijk aan {getal3} : {getal1 < getal3}")
print(f"{getal3} is kleiner dan of gelijk aan {getal1} : {getal3 < getal1}")
print(f"{getal1} is kleiner dan of gelijk aan {getal2} : {getal1 <= getal2}")

# Kijk of een string gelijk is aan een andere string
# John is gelijk aan John
# John is niet gelijk aan Doe
name = "John"
test = name
print(name is test)
print(name == "John")
print(name == "Doe")