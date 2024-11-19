def fibonacci(n):
    # Calcola il n-esimo numero della sequenza di Fibonacci usando la ricorsione
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    # Chiede all'utente quanti termini della sequenza vuole calcolare
    terms = int(input("Inserisci il numero di termini: "))
    
    # Genera e stampa la sequenza di Fibonacci
    sequence = [fibonacci(i) for i in range(terms)]
    print("Sequenza di Fibonacci:", ", ".join(map(str, sequence)))
