##Exercice Python 03 : Une Semaine de Températures 

temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]

##Question 1
moyenne = sum(temperatures) / len(temperatures)
minimum = min(temperatures)
maximum = max(temperatures)

print(f"Moyenne : {moyenne:.2f}")
print(f"Min : {minimum} / Max : {maximum}")

##Question 2
jours_chauds = 0

for temperature in temperatures:
    if temperature > 15:
        jours_chauds += 1

print(f"Jours > 15 °C : {jours_chauds}")

##Question 3
fahrenheit = [round(t * 9 / 5 + 32, 1) for t in temperatures]
print("Fahrenheit :", fahrenheit)

##Question 4 
for numero, temperature in enumerate(temperatures, start=1):
    print(f"Jour {numero} : {temperature} °C")
