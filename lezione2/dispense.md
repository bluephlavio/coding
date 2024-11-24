# Lezione 2: Modularità, Funzioni e Classi in Python

## Obiettivi della lezione

La **modularità** è un principio chiave per scrivere codice leggibile, riutilizzabile e manutenibile. In questa lezione approfondiremo:  
- Le **funzioni**, per suddividere il codice in blocchi logici e riutilizzabili.  
- Le **classi**, per strutturare dati e comportamento.  
- L'uso di **moduli** e **pacchetti**.  

---

## 1. Funzioni e Modularità

### Definizione di una funzione

Le **funzioni** permettono di isolare logiche specifiche e facilitare il riutilizzo:

```python
from math import pi

def calculate_circle_area(radius):
    return pi * radius**2

area = calculate_circle_area(5)
print(f"L'area del cerchio è {area}")
```

### Funzioni avanzate: argomenti opzionali e valore di default

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!
```

---

## 2. Classi: Organizzazione del codice con OOP

Le **classi** consentono di combinare dati e comportamenti:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(f"Rectangle area: {rect.area()}")
```

---

## 3. Moduli e Libreria Standard

### Moduli locali

Un **modulo** è un file Python (`.py`) che contiene funzioni e classi che possono essere importate in altri file.

**Esempio:**  
File `my_module.py`:

```python
def say_hello():
    print("Hello from my_module!")
```

File principale:

```python
import my_module

my_module.say_hello()
```

### Moduli della libreria standard

Python include una **libreria standard** ricca di moduli utili. Esempi:
- **`math`**: funzioni matematiche avanzate.
- **`random`**: generazione di numeri casuali.
- **`os`**: interazione con il sistema operativo.

**Esempio con `math`:**

```python
import math

print(math.sqrt(16))  # Output: 4.0
```

---

## Conclusioni

Abbiamo introdotto:
- L'importanza della **modularità** con funzioni e classi.  
- L'uso di **moduli locali** e della **libreria standard**.  

Questi strumenti sono essenziali per scrivere codice scalabile e manutenibile.

