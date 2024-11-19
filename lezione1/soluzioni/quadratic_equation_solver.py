# Risoluzione di equazioni di secondo grado (solo numeri reali)

# Chiediamo all'utente di inserire i coefficienti dell'equazione
a = float(input("Inserisci il coefficiente a: "))
b = float(input("Inserisci il coefficiente b: "))
c = float(input("Inserisci il coefficiente c: "))

# Calcoliamo il delta (discriminante) usando la formula delta = b^2 - 4ac
delta = b**2 - 4*a*c

# Controlliamo il segno del delta per determinare il numero e il tipo di radici
if delta > 0:
    # Se delta è positivo, l'equazione ha due radici reali distinte
    x1 = (-b + delta**0.5) / (2 * a)
    x2 = (-b - delta**0.5) / (2 * a)
    print(f"Le radici dell'equazione sono: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    # Se delta è zero, l'equazione ha una radice reale doppia
    x = -b / (2 * a)
    print(f"L'equazione ha una radice reale doppia: x = {x}")
else:
    # Se delta è negativo, l'equazione non ha radici reali
    print("L'equazione non ha radici reali.")
