import random

tal = random.randint(0, 100)
gisning_text = input("vilket tal tänker jag på?")
gisning=int(gisning_text)
if tal == gisning:
    print("du gisade rät")
if tal > gisning:
    gisning2 = input("det var fel talet är störe. gissa igen")
if tal < gisning:
    gisning2 = input("det ver fel talet är mindre. gissa igen")
else:
    print ("helt rätt")
if tal > gisning2:
    gisnin3 = input("det var fel talet är störe. gissa igen")
if tal < gisning2:
    gisning3 = input("det ver fel talet är mindre. gissa igen")
else:
    print ("helt rätt")