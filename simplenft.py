import random

nftface = [
    "    XXXbbbXXX   ",
]

eyes1 = [
    "  OOO     OOO  ",
    "  OOO     OOO  ",
]

eyes2 = [
    "  OOO     OOO  ",
    "  OOt     OOt  ",
]

eyes_gesamt = [eyes1,eyes2]

z = random.randint(0,1)
print(z)
augen = eyes_gesamt[z]

print(augen)