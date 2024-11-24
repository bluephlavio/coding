# Esercizi: Simulazioni con Sistemi di Particelle  

Questa serie di esercizi esplora la simulazione di sistemi di particelle utilizzando **ipycanvas**. Si parte dalla creazione di una libreria per rappresentare particelle e sistemi di particelle, per poi affrontare due simulazioni: un **gas di particelle** e il **problema degli n-corpi gravitazionale**.  

---

## 1. Creare una Libreria per Sistemi di Particelle  

### Obiettivo  
Creare una libreria Python che includa le seguenti classi:  
- **`Particle`**: rappresenta una particella con proprietà come posizione, velocità, massa e raggio. Deve includere metodi per aggiornare la posizione e verificare collisioni.  
- **`NParticlesSystem`**: rappresenta un sistema di più particelle, con metodi per evolvere il sistema nel tempo e gestire le interazioni tra particelle (come collisioni o forze).  

**Requisiti**:  
1. Scrivere il codice in un file chiamato `particles.py`.  
2. Definire un metodo `update(dt)` nella classe `NParticlesSystem` per aggiornare tutte le particelle nel sistema.  

---

## 2. Gas di Particelle  

### Obiettivo  
Simulare un **gas di particelle** in un contenitore rettangolare.  

**Requisiti**:  
1. Le particelle devono muoversi liberamente, rimbalzando sui bordi del contenitore.  
2. In caso di collisione tra particelle, applicare le leggi di conservazione della quantità di moto per calcolare le nuove velocità.  
3. Visualizzare la simulazione utilizzando **ipycanvas**.
---

## 3. Problema degli N-Corpi Gravitazionale  

### Obiettivo  
Simulare il movimento di particelle che si attraggono gravitazionalmente secondo la legge di gravitazione universale.  

$$
F = G \frac{m_1 m_2}{r^2}
$$ 

**Requisiti**:  
1. Estendere la classe `NParticlesSystem` per calcolare le forze gravitazionali tra le particelle.  
2. Aggiornare la posizione e la velocità di ciascuna particella in base alle forze calcolate.  
3. Visualizzare la simulazione con **ipycanvas**.  

**Estensione opzionale**:  
- Modificare i parametri del sistema, come il valore di $G$, il numero di particelle, o le masse delle particelle, e osservare come cambia la simulazione.  
- Salvare le traiettorie delle particelle e analizzarle in un notebook separato.  

---

## Consegna  

Per ciascun esercizio, implementare la soluzione in un notebook separato o in file Python, seguendo le specifiche indicate.  

