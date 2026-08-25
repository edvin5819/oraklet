
import random

svar = ["Ja, helt klart.", "Absolut", "såklartä.", "hundra procent.",]
fråga = input("fråga oraklet: ",)
print("du frågade:", fråga)
print(random.choice(svar))
