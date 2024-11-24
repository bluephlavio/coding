# Esercizi: Creare Animazioni e Simulazioni con ipycanvas  

Gli esercizi seguono un ordine di difficoltà crescente e sono progettati per consolidare i concetti fondamentali di **ipycanvas**, come il disegno di forme, il movimento e l'interazione.  

---

## 1. Movimento di una Particella  

Creare un'animazione in cui una particella si muove liberamente all'interno di un canvas rettangolare, rimbalzando quando tocca i bordi.  

**Istruzioni**:  
- Inizializzare la posizione e la velocità della particella.  
- Aggiornare la posizione della particella ad ogni frame.  
- Gestire i rimbalzi invertendo la velocità quando la particella raggiunge i bordi.  

**Estensione opzionale**: Aggiungere un'accelerazione costante verso il basso per simulare la **gravità**, e una perdita di energia sui rimbalzi riducendo la velocità verticale.  

---

## 2. Movimento Controllato  

Creare un'animazione in cui una particella si muove all'interno del canvas, controllata tramite i tasti direzionali della tastiera.  

**Istruzioni**:  
- Inizializzare la posizione della particella.  
- Gestire il movimento in base agli eventi dei tasti freccia (`ArrowUp`, `ArrowDown`, `ArrowLeft`, `ArrowRight`).  
- Limitare il movimento al canvas senza permettere alla particella di uscire dai bordi.  

**Estensione opzionale**: Aggiungere la possibilità di controllare la particella anche con il mouse.  

---

## 3. Random Walk  

Creare un'animazione in cui una particella esegue un **random walk**:  
- Ad ogni frame, la particella si sposta casualmente di una quantità fissa in una direzione casuale.  
- Disegnare il percorso della particella sul canvas, visualizzando il tracciato.  

**Estensione opzionale**:  
- Calcolare le distanze dall'origine per ogni posizione della particella e salvarle in un file CSV.  
- Analizzare i dati generati utilizzando **matplotlib**, visualizzando un grafico della distanza in funzione del tempo.  
