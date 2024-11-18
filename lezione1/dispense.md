# Lezione 1: Introduzione al Coding e a Python

## Obiettivi della lezione

Questa prima lezione ha l’obiettivo di introdurre i concetti fondamentali della programmazione, utilizzando Python come linguaggio di riferimento. Gli argomenti trattati saranno:
- Cos’è un **algoritmo** e come può essere utilizzato per risolvere problemi.
- Il ruolo dei **linguaggi di programmazione** come strumenti di comunicazione con il computer.
- La configurazione di un **ambiente di sviluppo**.
- Le basi della programmazione: **variabili**, **tipi di dati**, **input/output**.
- I concetti fondamentali di **condizionali** e **cicli**, utili per costruire programmi più complessi.

## Cos’è un algoritmo?

Si consideri il seguente scenario: un robot deve raggiungere una pianta specifica all’interno di una foresta. Per farlo, è necessario fornire al robot una sequenza precisa di istruzioni: 

1. Partire dal punto iniziale (una radura).
2. Camminare 10 metri verso nord.
3. Svoltare a destra e proseguire per altri 5 metri.
4. Raccogliere la pianta.

Questa serie di istruzioni costituisce un **algoritmo**: un insieme di passi chiari e ordinati che consente di raggiungere un obiettivo specifico.

Un algoritmo è:
- Una **sequenza di azioni** che risolve un problema.
- **Generale**, applicabile a problemi simili con poche modifiche.
- Fondamentale per descrivere processi naturali o simulazioni, come il moto di particelle o la crescita di popolazioni biologiche.

## Linguaggi di programmazione: il ponte tra umani e computer

I computer non comprendono il linguaggio naturale. Per interagire con loro, è necessario utilizzare i **linguaggi di programmazione**, che consentono di tradurre le istruzioni in un formato comprensibile alle macchine.

Durante il corso, verrà utilizzato **Python**, un linguaggio che combina semplicità e potenza.

**Perché Python è adatto alle scienze naturali?**
- **Semplice e leggibile**: consente di concentrarsi sulla logica del problema senza essere distratti da una sintassi complessa.
- **Ricco di librerie scientifiche**: include strumenti come `numpy` per l’algebra lineare, `matplotlib` per la visualizzazione e `scipy` per il calcolo scientifico.
- **Versatile**: adatto a numerosi ambiti, come la simulazione del moto dei pianeti, l’analisi di dati sperimentali o la modellazione di processi biologici.

Python permette di esplorare fenomeni naturali attraverso simulazioni, rendendo accessibili analisi complesse.

---

## Ambiente di sviluppo: GitHub Codespaces

Per scrivere ed eseguire codice, verrà utilizzato **GitHub Codespaces**, un ambiente di sviluppo cloud che funziona direttamente nel browser.

### Caratteristiche di GitHub Codespaces

GitHub Codespaces offre:
- **Un ambiente Python già configurato**, senza necessità di installare software aggiuntivo sul computer.
- **Integrazione con GitHub**, per salvare e condividere il lavoro in modo semplice.
- **Flessibilità**, consentendo l’accesso al codice da qualsiasi dispositivo connesso a Internet.

### Procedura di accesso a GitHub Codespaces
1. Accedere a [github.com](https://github.com) con le proprie credenziali.
2. Aprire il [repository del corso](github.com/bluephlavio/coding).
3. Creare una copia del repository cliccando su **Fork**.
3. Creare un nuovo Codespace selezionando **Code** > **Codespaces** > **Create Codespace**.

In pochi secondi, sarà disponibile un editor Python pronto per iniziare a scrivere il primo programma.

---

## Primo programma in Python: il classico “Hello World!”

Il primo passo per familiarizzare con un linguaggio di programmazione consiste nello scrivere un semplice programma che mostra un messaggio sullo schermo. In Python, questo può essere fatto con il seguente codice:

```python
print("Hello World!")
```

L’istruzione `print` consente di visualizzare del testo nella console. Questo programma, se eseguito, mostrerà il messaggio `Hello World!`.

Per essere eseguito da python il codice deve essere salvato in un file con estensione `.py` (es. `hello_world.py`) e lanciato dal terminale con il comando

```bash
python hello_world.py
```

---

## Basi della programmazione

### Variabili e tipi di dati

In ogni programma, è essenziale lavorare con i **dati**. Una **variabile** è uno spazio di memoria utilizzato per conservare un valore che può essere usato o modificato durante l’esecuzione del programma. In Python, la creazione di una variabile è semplice:

```python
name = "Alice"
age = 18
```

In questo caso:
- `name` è una variabile che contiene una **stringa** (testo).
- `age` è una variabile che contiene un **numero intero**.

Python supporta diversi tipi di dati fondamentali:
- **int**: numeri interi (`10`, `-3`).
- **float**: numeri decimali (`3.14`, `-0.5`).
- **str**: stringhe di testo (`"Ciao"`, `"Python"`).
- **bool**: valori booleani (`True`, `False`).

### Input e output

L’input permette di ricevere dati dall’utente, mentre l’output consente di visualizzare risultati.

Esempio di input e output:
```python
name = input("Inserisci il tuo nome: ")
print("Ciao, " + name + "!")
```
In questo caso, il programma chiede all’utente di inserire il proprio nome e successivamente lo utilizza per visualizzare un messaggio di saluto.

---

### Operatori

Gli operatori sono simboli che permettono di effettuare operazioni su variabili e valori. 

**Operatori aritmetici**:
- `+` (addizione)
- `-` (sottrazione)
- `*` (moltiplicazione)
- `/` (divisione)
- `//` (quoziente)
- `%` (resto)
- `**` (potenza)

Esempio:
```python
risultato = 5 + 3
print(risultato)  # Output: 8
```

**Operatori relazionali**:
- `==` (uguale a)
- `!=` (diverso da)
- `<`, `>`, `<=`, `>=` (minore, maggiore, minore o uguale, maggiore o uguale)

**Operatori logici**:
- `and`, `or`, `not`

Esempio:
```python
x = 10
y = 5
print(x > y and y > 0)  # Output: True
```

---

## Generazione di numeri casuali

In molti contesti scientifici e applicativi è utile poter generare numeri casuali. Python offre strumenti per farlo attraverso il modulo `random`. 

### Utilizzo di base

Per utilizzare numeri casuali, è necessario importare il modulo `random`. Un esempio semplice è la generazione di un numero intero casuale tra 1 e 10:

```python
import random

numero_casuale = random.randint(1, 10)
print("Il numero casuale generato è:", numero_casuale)
```

### Altre funzioni utili

- **`random.random()`**: genera un numero casuale tra 0 e 1.
- **`random.uniform(a, b)`**: genera un numero casuale a virgola mobile tra `a` e `b`.
- **`random.choice(lista)`**: seleziona casualmente un elemento da una lista.

Esempio:
```python
import random

scelta = random.choice(['rosso', 'verde', 'blu'])
print("Il colore scelto è:", scelta)
```

Queste funzioni saranno utili per creare simulazioni o giochi che richiedono variabilità.

---

## Condizionali: prendere decisioni

In molti programmi è necessario eseguire azioni diverse a seconda di determinate condizioni. Le **istruzioni condizionali** permettono di prendere decisioni.

Sintassi base:
```python
if condizione:
    # blocco di codice eseguito se la condizione è vera
elif altra_condizione:
    # blocco eseguito se la prima condizione è falsa ma questa è vera
else:
    # blocco eseguito se tutte le condizioni precedenti sono false
```

Esempio:
```python
age = int(input("Inserisci la tua età: "))

if age < 18:
    print("Sei minorenne.")
elif age == 18:
    print("Hai appena compiuto 18 anni!")
else:
    print("Sei maggiorenne.")
```

---

## Cicli iterativi: ripetere azioni

Spesso è necessario ripetere un’operazione più volte. I **cicli** permettono di farlo in modo efficiente.

### Ciclo `for`

Il ciclo `for` viene utilizzato per iterare su una sequenza (

come una lista o un intervallo di numeri).

Esempio:
```python
for i in range(5):
    print("Questo è il ciclo numero", i)
```
Il ciclo itererà 5 volte, con `i` che assumerà i valori da 0 a 4.

### Ciclo `while`

Il ciclo `while` esegue un blocco di codice finché una condizione rimane vera.

Esempio:
```python
x = 0
while x < 5:
    print("x è:", x)
    x += 1
```
Questo ciclo continuerà a eseguire il blocco finché `x` sarà minore di 5.
