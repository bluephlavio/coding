# Conteggio delle occorrenze in una frase

# Chiediamo all'utente di inserire una frase
phrase = input("Inserisci una frase: ")

# Creiamo un dizionario per tenere traccia delle occorrenze dei caratteri
occurrences = {}

# Iteriamo su ogni carattere della frase
for char in phrase:
    # Aggiorniamo il conteggio del carattere nel dizionario
    occurrences[char] = occurrences.get(char, 0) + 1

# Stampiamo il dizionario delle occorrenze
print("Occorrenze:", occurrences)
