# Lezione 2: Funzioni, Liste e Introduzione a Matplotlib

## Obiettivi della lezione

In questa seconda lezione si affrontano temi cruciali per la scrittura di programmi più modulari e strutturati. Verranno introdotti i concetti di **funzione**, **lista** e **dizionari**, per poi esplorare la visualizzazione dei dati con **Matplotlib**.

Gli obiettivi principali della lezione includono:
- Comprendere l'importanza delle **funzioni** per scrivere codice modulare e riutilizzabile.
- Gestire e manipolare **liste** per rappresentare e analizzare collezioni di dati.
- Introdurre i **dizionari** per associare chiavi a valori.
- Creare grafici semplici utilizzando la libreria **Matplotlib**.

---

## 1. Funzioni

Le **funzioni** permettono di raggruppare un insieme di istruzioni che possono essere eseguite più volte. Sono uno strumento fondamentale per la modularità e la leggibilità del codice.

### Definizione di una funzione

In Python, una funzione si definisce con la parola chiave `def`:

```python
def greet(name):
    print(f"Ciao, {name}!")
```

### Utilizzo delle funzioni

Per utilizzare una funzione, basta chiamarla specificando gli argomenti necessari:

```python
greet("Alice")  # Output: Ciao, Alice!
```

### Funzioni con valore di ritorno

Una funzione può anche restituire un valore usando la parola chiave `return`:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

---

## 2. Liste

Le **liste** sono strutture di dati fondamentali in Python, utili per memorizzare e manipolare collezioni ordinate di elementi.

### Creazione di una lista

Le liste si definiscono con le parentesi quadre `[]`:

```python
numbers = [1, 2, 3, 4, 5]
```

### Operazioni comuni sulle liste

- **Accesso agli elementi**:
  ```python
  print(numbers[0])  # Output: 1
  ```

- **Modifica degli elementi**:
  ```python
  numbers[2] = 10
  print(numbers)  # Output: [1, 2, 10, 4, 5]
  ```

- **Aggiungere elementi**:
  ```python
  numbers.append(6)
  ```

- **Rimuovere elementi**:
  ```python
  numbers.remove(10)
  ```

### Iterazione su una lista

È possibile scorrere gli elementi di una lista con un ciclo `for`:

```python
for num in numbers:
    print(num)
```

---

## 3. Dizionari

I **dizionari** sono strutture di dati che associano **chiavi** a **valori**.

### Creazione di un dizionario

I dizionari si definiscono con le parentesi graffe `{}`:

```python
student = {
    "name": "Alice",
    "age": 17,
    "class": "4A"
}
```

### Accesso e modifica

- **Accesso ai valori** tramite le chiavi:
  ```python
  print(student["name"])  # Output: Alice
  ```

- **Modifica di un valore**:
  ```python
  student["age"] = 18
  ```

---

## 4. Introduzione a Matplotlib

La libreria **Matplotlib** permette di creare grafici in modo semplice e intuitivo. È uno strumento essenziale per la visualizzazione dei dati.

### Creazione di un grafico semplice

Prima di iniziare, assicurarsi che la libreria sia installata. Se non lo è, utilizzare il comando:
```bash
pip install matplotlib
```

Ecco un esempio di utilizzo:

```python
import matplotlib.pyplot as plt

# Dati da visualizzare
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Creazione del grafico
plt.plot(x, y)

# Aggiunta di titolo e etichette
plt.title("Grafico di una funzione quadratica")
plt.xlabel("Asse X")
plt.ylabel("Asse Y")

# Mostrare il grafico
plt.show()
```

### Creazione di un istogramma

Gli istogrammi sono utili per visualizzare distribuzioni di dati:

```python
import matplotlib.pyplot as plt

# Dati per l'istogramma
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]

# Creazione dell'istogramma
plt.hist(data, bins=5, edgecolor="black")

# Aggiunta di titolo
plt.title("Istogramma dei dati")

# Mostrare l'istogramma
plt.show()
```

---

## Conclusioni

In questa lezione sono stati introdotti concetti chiave per la programmazione in Python:
- **Funzioni**, per modularizzare e riutilizzare il codice.
- **Liste** e **dizionari**, per la gestione di collezioni di dati.
- **Matplotlib**, per la visualizzazione grafica dei dati.

Nella prossima lezione, si approfondirà l’utilizzo di **Jupyter Notebook** e si inizieranno a esplorare simulazioni più avanzate come il **Random Walk**.