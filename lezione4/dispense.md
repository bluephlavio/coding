# Lezione 4: Introduzione a py5  

## Obiettivi della lezione  

In questa lezione esploreremo **py5**, una libreria Python ispirata al framework **Processing**, ideale per creare sketch grafici interattivi e dinamici. Impareremo i concetti fondamentali per lavorare con py5 e costruiremo animazioni e simulazioni visive.  

Gli obiettivi principali della lezione sono:  
- Capire la struttura di base di uno sketch py5: **setup**, **draw** e **settings**.  
- Conoscere le funzioni principali per disegnare e muovere oggetti nel canvas.  
- Comprendere come manipolare variabili per creare movimento e interattività.  

---

## 1. Struttura di Base di uno Sketch py5  

Un programma py5 è composto da tre funzioni principali:  

1. **`settings()`** *(opzionale)*: utilizzata per configurare le proprietà avanzate del canvas. Deve essere definita se si desidera usare funzioni come `py5.size()` per impostare le dimensioni del canvas.  
2. **`setup()`**: viene eseguita una volta all’inizio del programma. Si usa per configurare l’ambiente, ad esempio impostando il colore di sfondo o inizializzando le variabili.  
3. **`draw()`**: viene eseguita in un ciclo continuo per creare animazioni o aggiornare lo stato dello sketch.  

Esempio base:  

```python
import py5

def settings():
    py5.size(800, 600)  # Imposta le dimensioni del canvas

def setup():
    py5.background(200)  # Colore di sfondo (grigio chiaro)

def draw():
    py5.fill(255, 0, 0)  # Colore di riempimento (rosso)
    py5.circle(py5.mouse_x, py5.mouse_y, 50)  # Disegna un cerchio che segue il mouse

py5.run_sketch()
```

---

## 2. Disegnare con py5  

py5 offre una varietà di funzioni per disegnare forme geometriche sul canvas.  

### 2.1 Forme Base  

- **Cerchi e ellissi**:  
  ```python
  py5.circle(x, y, diameter)
  py5.ellipse(x, y, width, height)
  ```  

- **Rettangoli e linee**:  
  ```python
  py5.rect(x, y, width, height)
  py5.line(x1, y1, x2, y2)
  ```  

- **Punti e poligoni**:  
  ```python
  py5.point(x, y)
  py5.begin_shape()
  py5.vertex(x1, y1)
  py5.vertex(x2, y2)
  py5.end_shape()
  ```  

### 2.2 Colori e Stili  

- **Riempimento e contorni**:  
  ```python
  py5.fill(r, g, b)  # Colore di riempimento
  py5.stroke(r, g, b)  # Colore del contorno
  py5.no_fill()  # Nessun riempimento
  py5.no_stroke()  # Nessun contorno
  ```  

- **Sfondo**:  
  ```python
  py5.background(r, g, b)  # Imposta il colore di sfondo
  ```

---

## 3. Movimento e Interattività  

### 3.1 Gestire il Movimento  

Per creare movimento in py5, si aggiornano le coordinate degli oggetti in modo continuo nella funzione `draw()`.  

Esempio:  

```python
x, y = 100, 100  # Posizione iniziale
velocity_x, velocity_y = 2, 3  # Velocità iniziale

def draw():
    global x, y
    x += velocity_x  # Aggiorna la posizione
    y += velocity_y
    py5.circle(x, y, 20)  # Disegna il cerchio in movimento
```

### 3.2 Gestire i Rimbalzi  

Quando un oggetto tocca il bordo del canvas, è necessario invertire la direzione della velocità:  

```python
if x <= 0 or x >= py5.width:
    velocity_x *= -1
if y <= 0 or y >= py5.height:
    velocity_y *= -1
```

---

## 4. Salvare i Dati  

py5 permette di salvare dati generati durante lo sketch, ad esempio posizioni o velocità, in un file.  

Esempio di salvataggio dati:  

```python
positions = []  # Lista per salvare le posizioni

def draw():
    global positions
    positions.append(f"{x},{y}")  # Salva la posizione
    if len(positions) >= 100:  # Dopo 100 frame
        py5.save_strings("positions.csv", positions)  # Salva su file
        py5.no_loop()  # Ferma lo sketch
```

---

## Conclusione  

In questa lezione abbiamo visto le basi di py5, dalla struttura di uno sketch alle funzioni principali per disegnare e creare movimento. Questi strumenti saranno essenziali per sviluppare simulazioni dinamiche e rappresentazioni creative.  