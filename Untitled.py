
import random

svar = ["Ja, helt klart.", "Absolut", "såklart.", "hundra procent.","nej.",]
fråga = input("fråga oraklet: ",)
print("du frågade:", fråga)
print(random.choice(svar))
