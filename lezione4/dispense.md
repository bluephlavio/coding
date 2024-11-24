# Lezione 4: Introduzione a ipycanvas  

## Obiettivi della lezione  

In questa lezione esploreremo **ipycanvas**, una libreria Python progettata per creare animazioni e grafica interattiva all'interno di un notebook Jupyter. L'obiettivo principale sarà imparare a simulare e animare il movimento di una particella nel canvas, utilizzando concetti fondamentali come il disegno, la gestione degli eventi e l'aggiornamento continuo dello stato.  

### Argomenti principali:  
- Introduzione a ipycanvas: configurazione e utilizzo di base.  
- Creare animazioni utilizzando cicli di aggiornamento continui.  
- Gestire il movimento della particella: libero, controllato, casuale.  
- Salvare dati generati dalle simulazioni e analizzarli.  

---

## 1. Introduzione a ipycanvas  

**ipycanvas** è una libreria Python che permette di creare grafica 2D direttamente in un notebook Jupyter. Il componente principale è il canvas, su cui possiamo disegnare forme e aggiornare il contenuto dinamicamente.  

### 1.1 Creazione di un Canvas  

Per iniziare, è necessario importare la libreria e creare un canvas:  

```python
from ipycanvas import Canvas

# Creazione di un canvas 400x400
canvas = Canvas(width=400, height=400)
canvas
```  

---

## 2. Disegnare nel Canvas  

ipycanvas fornisce una serie di metodi per disegnare forme geometriche, impostare colori e gestire il contesto grafico.  

### 2.1 Forme Base  

- **Cerchi**:  
  ```python
  canvas.fill_circle(x, y, radius)
  ```  

- **Rettangoli**:  
  ```python
  canvas.fill_rect(x, y, width, height)
  ```  

- **Linee**:  
  ```python
  canvas.stroke_line(x1, y1, x2, y2)
  ```  

### 2.2 Colori  

- Impostare il colore di riempimento:  
  ```python
  canvas.fill_style = "red"
  ```  

- Impostare il colore delle linee:  
  ```python
  canvas.stroke_style = "blue"
  ```  

### 2.3 Pulire il Canvas  

Per pulire il canvas, si utilizza:  
```python
canvas.clear()
```  

---

## 3. Creare Animazioni  

Per creare animazioni, è necessario aggiornare continuamente lo stato del canvas. Questo si ottiene combinando:  
1. **Un loop di aggiornamento**, che disegna e aggiorna la scena ad ogni frame.  
2. **Il metodo `hold_canvas()`**, per migliorare le performance durante gli aggiornamenti.  

Esempio base:  
```python
from ipycanvas import hold_canvas

# Disegna e aggiorna in un ciclo
def update():
    with hold_canvas(canvas):
        canvas.clear()
        canvas.fill_circle(200, 200, 50)
```  

---

## 4. Interazione con la Tastiera  

ipycanvas permette di gestire eventi di tastiera e mouse.  

### 4.1 Eventi di Tastiera  

È possibile catturare eventi di tastiera e utilizzare i tasti per controllare gli oggetti:  
```python
@canvas.on_key_down
def handle_key(event):
    print(f"Tasto premuto: {event.key}")
```  

### 4.2 Eventi del Mouse  

Analogamente, si possono catturare eventi del mouse:  
```python
@canvas.on_mouse_down
def handle_mouse(event):
    print(f"Clic su: {event.x}, {event.y}")
```  

---

## 5. Salvare e Analizzare Dati  

Un aspetto importante delle simulazioni è la possibilità di salvare dati per analisi successive. Ad esempio, si possono registrare le posizioni di una particella e salvarle in un file CSV:  

```python
import csv

positions = [(100, 100), (110, 105), (120, 110)]  # Esempio di dati

# Salva le posizioni in un file CSV
with open("positions.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["x", "y"])
    writer.writerows(positions)
```  

Questi dati possono poi essere analizzati utilizzando librerie come **matplotlib**.  

---

## Conclusione  

In questa lezione abbiamo imparato a utilizzare ipycanvas per creare animazioni e interazioni grafiche in un notebook Jupyter. Queste basi saranno fondamentali per sviluppare simulazioni più complesse nelle lezioni successive.

