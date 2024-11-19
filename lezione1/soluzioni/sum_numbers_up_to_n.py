# Programma per calcolare la somma dei numeri da 1 a N

# Input: chiedere all'utente un numero intero positivo
N = int(input("Inserisci un numero: "))

# Calcolo della somma dei numeri da 1 a N
total_sum = 0
for i in range(1, N + 1):
    total_sum += i

# Output: mostrare la somma
print(f"La somma dei numeri da 1 a {N} è {total_sum}.")
