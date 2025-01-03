import tkinter as tk
from tkinter import Entry, Label


def bmi(poids, taille=1.8):
    bmi = poids / (taille ** 2)
    donnees = {'Poids': poids, 'Taille ': taille, 'IMC ': round(bmi, 2)}
    print(f"Etat de forme : {imc_signe(bmi)}")
    return donnees


def imc_signe(bmi):
    message = ""
    if bmi < 16:
        message = "Anorexie ou dénutrition"
    elif 16 <= bmi < 18:
        message = "Maigreur"
    elif 18 <= bmi < 25:
        message = "Corpulence normale"
    elif 25 <= bmi < 30:
        message = "Surpoids"
    elif 30 <= bmi < 35:
        message = "Obésité modérée"
    elif 35 <= bmi < 40:
        message = "Obésité élevée"
    else:
        message = "Obésite morbide ou massive"
    return message


root = tk.Tk()
root.title('BMI simple app')
root.geometry("600x300")
tk.Label(root, text="Appli Suivi Santé")

entry = Entry(root, width=30)
entry.pack()
test = entry.get()
label = Label(root, text=test)
label.pack()
tk.Button(root, text="Fermer", command=root.quit).pack()
root.mainloop()

# poids = float(input("Votre poids : "))
# fab = bmi(poids)
# print(f"{fab}")
# perte = 97.2 - poids
# if perte >= 0:
#    print(f"Vous avez perdu {round(perte, 2)}kg")
# else:
#   print(f"Vous avez pris {round(perte, 2)}kg !!!")
