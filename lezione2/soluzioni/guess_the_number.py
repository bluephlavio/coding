import random

def guess_number_game():
    # Genera un numero casuale tra 1 e 100
    secret_number = random.randint(1, 100)
    attempts = 0  # Conta il numero di tentativi

    print("Ho scelto un numero tra 1 e 100. Prova a indovinarlo!")
    
    while True:
        # Chiede all'utente di inserire un numero
        guess = int(input("Inserisci il tuo numero: "))
        attempts += 1
        
        # Fornisce suggerimenti all'utente
        if guess < secret_number:
            print("Troppo basso!")
        elif guess > secret_number:
            print("Troppo alto!")
        else:
            # L'utente ha indovinato il numero
            print(f"Hai indovinato! Il numero era {secret_number}.")
            break

    # Calcola un indice di fortuna basato sul numero di tentativi
    if attempts <= 5:
        luck_index = "Molto Fortunato!"
    elif attempts <= 10:
        luck_index = "Fortunato!"
    else:
        luck_index = "Sfortunato!"
    
    print(f"Indice di fortuna: {attempts} tentativi ({luck_index})")

if __name__ == "__main__":
    # Avvia il gioco
    guess_number_game()
