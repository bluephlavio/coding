# Programma per indovinare un numero casuale tra 1 e 10

import random

# Genera un numero casuale tra 1 e 10
random_number = random.randint(1, 10)

# Input: chiedere all'utente di indovinare il numero
user_guess = int(input("Indovina un numero tra 1 e 10: "))

# Verifica se l'utente ha indovinato
if user_guess == random_number:
    print("Bravo, hai indovinato!")
else:
    print(f"Peccato, il numero corretto era {random_number}.")
