# Programma per determinare se un numero è pari o dispari

# Input: chiedere all'utente un numero intero
number = int(input("Inserisci un numero: "))

# Verifica se il numero è pari o dispari
if number % 2 == 0:
    print(f"Il numero {number} è pari.")
else:
    print(f"Il numero {number} è dispari.")
