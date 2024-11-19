def factorial(n):
    # Calcola il fattoriale di un numero intero positivo
    result = 1
    # Itera da 2 fino a n, moltiplicando i valori successivi
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    # Chiede all'utente un numero intero positivo
    number = int(input("Inserisci un numero: "))
    # Calcola e stampa il fattoriale
    print(f"Il fattoriale di {number} è {factorial(number)}.")
