# Lezione 5: Simulazioni con Sistemi di Particelle  

## Obiettivi della lezione  

In questa lezione esploreremo come passare dalle animazioni di una singola particella alla simulazione di un sistema con **n particelle**. Ci concentreremo su:  
1. La progettazione e implementazione di una libreria Python per rappresentare particelle e sistemi di particelle.  
2. L’utilizzo di **ipycanvas** per animare e visualizzare le simulazioni.  
3. Concetti base di **programmazione orientata agli oggetti (OOP)** per estendere la libreria a problemi specifici, come il gas di particelle o il problema degli **n-corpi gravitazionale**.  

---

## 1. Creazione della Libreria  

Per gestire sistemi complessi, è utile definire una struttura modulare e riutilizzabile. La libreria sarà composta da:  

- **`Particle`**: una classe che rappresenta una singola particella con proprietà come posizione, velocità, massa e raggio.  
- **`NParticlesSystem`**: una classe che rappresenta un sistema di più particelle e fornisce metodi per evolvere il sistema nel tempo.  

Esempio di struttura base:  
```python
class Particle:
    def __init__(self, x, y, vx, vy, mass, radius):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.radius = radius

    def update_position(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
```

```python
class NParticlesSystem:
    def __init__(self, particles):
        self.particles = particles

    def update(self, dt):
        for particle in self.particles:
            particle.update_position(dt)
```  

---

## 2. Simulazioni di Gas di Particelle  

La prima applicazione sarà simulare un **gas di particelle** in un contenitore rettangolare. Le particelle si muoveranno liberamente, rimbalzando sui bordi e tra di loro in caso di collisione.  

### Obiettivi della simulazione  
- Gestire le collisioni tra particelle utilizzando le leggi di conservazione della quantità di moto.  
- Visualizzare il movimento delle particelle in un canvas con **ipycanvas**.  

---

## 3. Simulazione del Problema degli N-Corpi  

Il problema degli **n-corpi gravitazionale** studia l'interazione di particelle che si attraggono reciprocamente secondo la legge di gravitazione universale:  
\[
F = G \frac{m_1 m_2}{r^2}
\]  

### Obiettivi della simulazione  
- Calcolare la forza gravitazionale tra ogni coppia di particelle.  
- Aggiornare la posizione e la velocità delle particelle in base alle forze calcolate.  
- Visualizzare il sistema in evoluzione con **ipycanvas**.  

---

## 4. Concetti di Programmazione Orientata agli Oggetti  

Le simulazioni complesse richiedono una struttura ben organizzata. La **programmazione orientata agli oggetti (OOP)** offre strumenti per:  
- **Incapsulamento**: raggruppare proprietà e metodi legati a un’entità.  
- **Ereditarietà**: riutilizzare e personalizzare il comportamento di una classe.  

### Estendere la Classe `NParticlesSystem`  
Ad esempio, per creare un sistema con particelle che si attraggono gravitazionalmente, possiamo estendere `NParticlesSystem`:  

```python
class GravitationalSystem(NParticlesSystem):
    def __init__(self, particles, G):
        super().__init__(particles)
        self.G = G

    def update(self, dt):
        # Calcola le forze gravitazionali
        for particle in self.particles:
            # Aggiorna posizione e velocità
            pass
```

---

## 5. Simulazioni Interattive  

Con **ipycanvas**, è possibile creare animazioni per visualizzare l’evoluzione di sistemi di particelle:  
- Disegnare ogni particella come un cerchio con una dimensione proporzionale al raggio.  
- Utilizzare un **loop di aggiornamento continuo** per animare il sistema.  

Esempio di animazione:  
```python
from ipycanvas import Canvas

canvas = Canvas(width=400, height=400)

def update():
    canvas.clear()
    for particle in particles:
        canvas.fill_circle(particle.x, particle.y, particle.radius)

# Avvia l’animazione
anim = Animation(canvas, update)
anim.start()
```

---

## Conclusione  

Questa lezione ha introdotto i concetti necessari per simulare sistemi di particelle, passando da animazioni semplici a simulazioni fisiche più complesse. Nelle esercitazioni, metteremo in pratica questi concetti per creare un gas di particelle e un sistema gravitazionale interattivo.  
