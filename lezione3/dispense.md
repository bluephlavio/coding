# Lezione 3: Introduzione a Jupyter Notebook, numpy, pandas e matplotlib

## Obiettivi della lezione

In questa lezione esploreremo:  
- L'uso di **Jupyter Notebook** come ambiente interattivo integrato in **VSCode**.  
- La libreria **numpy** per operazioni matematiche e gestione di array.  
- La libreria **pandas** per la gestione di dati tabellari.  
- La libreria **matplotlib** per la creazione di grafici e la visualizzazione dei dati.  

---

## 1. Jupyter Notebook

**Jupyter Notebook** permette di combinare codice eseguibile, testo formattato, grafici e altro in un unico documento interattivo.

### 1.1 Avviare un Notebook in VSCode

In **GitHub Codespaces**, non è necessario lanciare Jupyter Notebook manualmente. **VSCode** fornisce un'integrazione diretta:  
1. Aprire un file `.ipynb` direttamente in VSCode.  
2. L'interfaccia di editing e le celle saranno pronte per l'uso.  

### 1.2 Celle di codice e markdown

- **Cella di codice**: per scrivere ed eseguire codice Python.  
- **Cella di testo**: per inserire note, spiegazioni e istruzioni usando il formato **Markdown**.  

---

## 2. numpy: Operazioni matematiche e array

La libreria **numpy** è fondamentale per il calcolo scientifico in Python.

### 2.1 Creare e manipolare array

Esempio di creazione e operazioni base con array:

```python
import numpy as np

# Creare un array
a = np.array([1, 2, 3, 4, 5])

# Operazioni matematiche
print(a * 2)  # Moltiplicazione elemento per elemento
print(a + 3)  # Somma elemento per elemento
print(np.sqrt(a))  # Radice quadrata elemento per elemento
```

---

## 3. pandas: Gestione di dati e tabelle

La libreria **pandas** consente di lavorare facilmente con dati strutturati come tabelle.

### 3.1 Lettura e scrittura di file CSV

Esempio di lettura di un file CSV:

```python
import pandas as pd

# Leggere un file CSV
df = pd.read_csv('data.csv')
print(df.head())

# Operazioni sui dati
print(df['colonna'].mean())  # Calcolo della media di una colonna
```

### 3.2 Modifica e salvataggio dei dati

Esempio di modifica e salvataggio:

```python
# Creare una nuova colonna
df['nuova_colonna'] = df['colonna'] * 2

# Salvare il file modificato
df.to_csv('processed_data.csv', index=False)
```

---

## 4. matplotlib: Visualizzare dati con grafici

La libreria **matplotlib** è uno strumento fondamentale per creare grafici di alta qualità in Python.

### 4.1 Creare un grafico semplice

Esempio di grafico lineare:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title("Esempio di Grafico Lineare")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
```

### 4.2 Istogrammi

Esempio di creazione di un istogramma:

```python
import numpy as np

data = np.random.randn(1000)  # Generare dati casuali

plt.hist(data, bins=20, edgecolor='black', color='skyblue')
plt.title("Istogramma")
plt.xlabel("Valori")
plt.ylabel("Frequenza")
plt.show()
```

---

## Conclusione

Questa lezione ha introdotto strumenti fondamentali per l'analisi e la visualizzazione dei dati: **Jupyter Notebook**, **numpy**, **pandas**, e **matplotlib**. Approfondite questi strumenti per sviluppare competenze essenziali nell'analisi dei dati e nella programmazione scientifica.

