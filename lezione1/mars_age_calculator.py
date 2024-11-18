# Programma per calcolare l'età equivalente su Marte

# Costante: un anno su Marte in giorni terrestri
MARS_YEAR_DAYS = 687

# Costante: un anno sulla Terra in giorni terrestri
EARTH_YEAR_DAYS = 365

# Input: chiedere all'utente la propria età in anni terrestri
earth_age = float(input("Inserisci la tua età in anni terrestri: "))

# Calcolo: convertire l'età terrestre in giorni e calcolare l'equivalente su Marte
earth_age_in_days = earth_age * EARTH_YEAR_DAYS
mars_age = earth_age_in_days / MARS_YEAR_DAYS

# Output: mostrare l'età equivalente su Marte
print(f"Su Marte avresti circa {mars_age:.2f} anni.")
