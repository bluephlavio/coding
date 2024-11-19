# Esercizi: Applicare Funzioni, Classi, Moduli e Pandas

Gli esercizi seguono un ordine di difficoltà crescente e sono in linea con i concetti di modularità, funzioni e classi. Inoltre, si esplora l'uso di **pandas** per la gestione di dati da file e di **random** per la generazione casuale.

---

## 1. Calcolo del fattoriale

Scrivere una funzione che calcoli il **fattoriale** di un numero intero positivo utilizzando un ciclo `for`.

**Esempio di output**:
```
Inserisci un numero: 5
Il fattoriale di 5 è 120.
```

---

## 2. Sequenza di Fibonacci

Scrivere una funzione ricorsiva che generi i primi `N` numeri della **sequenza di Fibonacci**. 

**Esempio di output**:
```
Inserisci il numero di termini: 10
Sequenza di Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
```

---

## 3. Indovina il numero

Scrivere un gioco in cui il programma genera un numero casuale tra 1 e 100. L'utente deve indovinare il numero, con suggerimenti forniti ad ogni tentativo ("Troppo alto" o "Troppo basso"). Alla fine, il programma assegna un **indice di fortuna** basato sul numero di tentativi.

**Esempio di output**:
```
Ho scelto un numero tra 1 e 100. Prova a indovinarlo!
Inserisci il tuo numero: 50
Troppo alto! Prova ancora.
Inserisci il tuo numero: 25
Troppo basso! Prova ancora.
...
Hai indovinato! Il numero era 42.
Indice di fortuna: 7 (Molto Fortunato!)
```

---

## 4. Simulazione di un lancio di dadi

Scrivere una classe `DiceSimulator` che simuli il lancio di un dado a sei facce. L'utente può scegliere il numero di lanci. Il programma calcola e mostra la frequenza di ciascun numero ottenuto e alcune statistiche.

**Esempio di output**:
```
Quanti lanci vuoi simulare? 100
Occorrenze 1: 18 volte
Occorrenze 2: 15 volte
Occorrenze 3: 17 volte
Occorrenze 4: 14 volte
Occorrenze 5: 20 volte
Occorrenze 6: 16 volte
Media: 3.51
Deviazione standard: 1.73
```

---

## 5. Calcolo di π con Monte Carlo

Scrivere un programma che utilizzi il **metodo Monte Carlo** per stimare il valore di π. Simulare il lancio di punti casuali all'interno di un quadrato di lato 2 e verificare quanti di questi cadono all'interno di un cerchio di raggio 1.

**Esempio di output**:
```
Inserisci il numero di punti da simulare: 10000
Valore stimato di π: 3.1412
```

---

### 6. Periodo del pendolo e $g$

In un esperimento di laboratorio si misura il periodo $T$ di un pendolo semplice per diverse lunghezze $L$, ripetendo più volte ogni misura. Ogni misurazione è accompagnata da un’incertezza sperimentale.

Scrivere un programma che:  
1. Legga i dati da un file `data.csv` contenente le colonne:
   - `lunghezza`: lunghezza del pendolo (in metri);
   - `periodo`: periodo misurato (in secondi);
   - `incertezza_periodo`: incertezza associata al periodo misurato.
2. Calcoli il **valore medio del periodo** $T$ per ciascuna lunghezza.
3. Calcoli il valore medio dell'accelerazione di gravità $g$ usando la formula:
   $$
   g = \frac{4\pi^2 L}{T^2}
   $$ 
4. Calcoli l’**incertezza su $g$** propagando l’incertezza del periodo.  
5. Salvi i risultati in un nuovo file `processed_data.csv` contenente le colonne:  
   - `lunghezza`  
   - `periodo`  
   - `g`
   - `incertezza_g`.

**Esempio di `data.csv`**:  
```
lunghezza,periodo,incertezza_periodo
1.0,2.02,0.01
1.0,2.03,0.01
1.0,2.01,0.01
1.5,2.46,0.02
1.5,2.47,0.02
1.5,2.48,0.02
```

**Esempio di output (`processed_data.csv`)**:  
```
lunghezza,periodo,g,incertezza_g
1.0,2.02,9.70,0.10
1.5,2.47,9.78,0.12
```

**Esempio di output in console**:  
```
File processed_data.csv creato con i risultati elaborati.
```