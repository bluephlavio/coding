import random

class GuessNumberGame:
    # Inizializza il numero segreto e il contatore dei tentativi
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    # Metodo principale per giocare
    def play(self):
        print("Ho scelto un numero tra 1 e 100. Prova a indovinarlo!")
        
        while True:
            try:
                guess = int(input("Inserisci il tuo numero: "))
                self.attempts += 1
                if guess < self.secret_number:
                    print("Troppo basso!")
                elif guess > self.secret_number:
                    print("Troppo alto!")
                else:
                    print(f"Hai indovinato! Il numero era {self.secret_number}.")
                    break
            except ValueError:
                print("Per favore, inserisci un numero valido.")
        
        self.display_luck_index()

    # Metodo per calcolare e visualizzare l'indice di fortuna
    def display_luck_index(self):
        if self.attempts <= 5:
            luck_index = "Molto Fortunato!"
        elif self.attempts <= 10:
            luck_index = "Fortunato!"
        else:
            luck_index = "Sfortunato!"
        
        print(f"Indice di fortuna: {self.attempts} tentativi ({luck_index})")

if __name__ == "__main__":
    # Crea un'istanza della classe e avvia il gioco
    game = GuessNumberGame()
    game.play()
