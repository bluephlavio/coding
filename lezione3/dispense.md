# Lezione 3: Introduzione a Jupyter Notebook, matplotlib e py5

## Obiettivi della lezione

In questa lezione esploreremo:
- L'uso di **Jupyter Notebook** come ambiente interattivo integrato in **VSCode**.
- La libreria **matplotlib** per la creazione di grafici e la visualizzazione dei dati.
- Un'introduzione a **py5** per la generazione di grafica interattiva.

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

## 2. matplotlib: Visualizzare dati con grafici

La libreria **matplotlib** è uno strumento fondamentale per creare grafici di alta qualità in Python.

### 2.1 Installazione e primo grafico

matplotlib è preinstallato in Codespaces. Per verificarne l'uso, ecco un esempio base di grafico:

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

### 2.2 Compito: Personalizzare i grafici

Esplorare diverse personalizzazioni:
- Modificare colori e stili di linea.
- Aggiungere legende e annotazioni.
- Creare istogrammi o grafici a barre.

---

## 3. py5: Introduzione alla grafica interattiva

**py5** consente di creare sketch grafici dinamici e interattivi, ispirati al framework Processing.

### 3.1 Installazione

Per installare py5:
```bash
pip install py5
```

### 3.2 Primo Sketch: Disegno Statico

Ecco un esempio per tracciare semplici cerchi in una finestra:

```python
import py5

def setup():
    py5.size(500, 500)
    py5.background(200)

def draw():
    py5.fill(100, 200, 150)
    py5.circle(py5.mouse_x, py5.mouse_y, 20)
```

### 3.3 Compito: Esplorare sketch dinamici

- Modificare lo sketch per cambiare colori e forme in base alla posizione del mouse o al tempo.
- Utilizzare il metodo `py5.random()` per introdurre variabilità.

---

## Conclusione

Questa lezione ha introdotto strumenti potenti per scrivere codice interattivo e visualizzare dati. Approfondite **matplotlib** e **py5** per ampliare le vostre competenze nella visualizzazione e nel creative coding.
