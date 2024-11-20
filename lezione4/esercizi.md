# Esercizi: Creare Animazioni e Simulazioni con py5  

Gli esercizi seguono un ordine di difficoltà crescente e sono progettati per consolidare i concetti fondamentali di **py5**, come il disegno di forme, il movimento, e l'interazione.  

---

## 1. Movimento di una Particella  

Creare uno sketch in cui una particella (rappresentata da un cerchio) si muove nel canvas, rimbalzando quando raggiunge i bordi.  

**Istruzioni**:  
- Inizializzare la posizione e la velocità della particella.  
- Aggiornare la posizione della particella in `draw()`.  
- Gestire i rimbalzi invertendo la velocità quando la particella tocca i bordi.

---

## 2. Movimento con Gravità  

Estendere l’esercizio precedente aggiungendo l’effetto della **gravità**:  
- Applicare un'accelerazione costante verso il basso.  
- Gestire il rimbalzo sul bordo inferiore, riducendo la velocità verticale per simulare la perdita di energia (es. moltiplicando la velocità per un coefficiente \( < 1 \)).  

**Estensione opzionale**: Aggiungere un controllo per arrestare la particella quando la sua velocità è troppo bassa.  

---

## 3. Gas di Particelle  

Creare uno sketch in cui **più particelle** si muovono nel canvas rimbalzando sui bordi.  

**Istruzioni**:  
- Inizializzare più particelle con posizioni e velocità casuali.  
- Aggiornare la posizione di ogni particella in `draw()`.  
- Disegnare tutte le particelle sul canvas.  

---

## 4. Random Walk  

Creare uno sketch in cui una particella esegue un **random walk**:  
- Ad ogni frame, la particella si sposta casualmente di una quantità fissa in una direzione casuale.  
- Disegnare il percorso della particella sul canvas.  

**Estensione opzionale**:  
- Salvare le distanze dall'origine in un file CSV.  
- Analizzare i dati generati utilizzando **matplotlib** in un notebook separato.
