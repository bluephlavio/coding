# Programma per stampare tutti i numeri primi da 1 a N separati da virgole

# Input: chiedere all'utente un numero intero positivo
N = int(input("Inserisci un numero: "))

# Calcolo e costruzione della stringa dei numeri primi da 1 a N
prime_numbers = ""
for num in range(1, N + 1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        if prime_numbers:  # Aggiunge una virgola solo se la stringa non è vuota
            prime_numbers += ", "
        prime_numbers += str(num)

# Output: mostrare i numeri primi
print(f"I numeri primi da 1 a {N} sono: {prime_numbers}")
