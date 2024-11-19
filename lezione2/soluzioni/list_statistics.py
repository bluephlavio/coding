# Programma per calcolare statistiche su una lista di numeri

import math

# Input: chiedere una stringa di numeri separati da virgole
numbers = input("Inserisci una serie di numeri separati da virgole: ")
numbers_list = [int(x) for x in numbers.split(",")]

# Calcolo delle statistiche
max_num = max(numbers_list)
min_num = min(numbers_list)
mean = sum(numbers_list) / len(numbers_list)
semi_dispersion = max_num - mean
variance = sum((x - mean) ** 2 for x in numbers_list) / len(numbers_list)
std_deviation = math.sqrt(variance)

# Output delle statistiche
print(f"Il massimo è {max_num}")
print(f"Il minimo è {min_num}")
print(f"La media è {mean:.2f}")
print(f"La semidispersione massima è {semi_dispersion:.2f}")
print(f"La deviazione standard è {std_deviation:.3f}")
