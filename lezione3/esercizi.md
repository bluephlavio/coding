# Esercizi: Analisi e Visualizzazione Dati con numpy, pandas e matplotlib

Gli esercizi seguono un ordine di difficoltà crescente e sono in linea con i concetti introdotti nella lezione: utilizzo di **numpy**, **pandas**, e **matplotlib** per analisi e visualizzazione dei dati.

---

## 1. Grafico della Successione di Fibonacci

Scrivere una funzione che generi i primi `N` numeri della **successione di Fibonacci** e utilizzi **matplotlib** per rappresentarli graficamente.

**Istruzioni**:  
- L'asse x rappresenta l'indice dei termini.  
- L'asse y rappresenta i valori della successione.  
- Aggiungere un titolo e le etichette degli assi.  

**Esempio di output**:  
Un grafico a linee che mostra la crescita esponenziale dei termini della successione di Fibonacci.

---

## 2. Istogramma di Numeri Casuali

Generare 1000 numeri casuali da una distribuzione uniforme tra 0 e 1 e rappresentarli con un **istogramma**. Successivamente:  
- Ripetere il grafico per una distribuzione normale con media 0 e deviazione standard 1.  
- Aggiungere la curva teorica della distribuzione sovrapposta all'istogramma.  

**Istruzioni**:  
- Utilizzare **numpy** per generare i numeri casuali.  
- Personalizzare i grafici con titoli, etichette e griglie.  

**Esempio di output**:  
Due istogrammi con frequenze relative e curve teoriche delle distribuzioni.

---

## 3. Relazione Lunghezza-Periodo del Pendolo

Riprendere il problema del **pendolo semplice** e graficare la relazione tra la lunghezza del pendolo $L$ e il periodo $T$. Utilizzare i dati forniti in un file `data.csv`.  

**Istruzioni**:  
1. Utilizzare **pandas** per leggere i dati dal file.  
2. Calcolare i valori medi e le incertezze su $T$ per ogni lunghezza $L$.  
3. Calcolare $g$ e $\Delta g$ e salvarli in un nuovo file `processed_data.csv`.  
4. Utilizzare **matplotlib** per rappresentare graficamente la relazione $L$-$T$ e sovrapporre la curva teorica del periodo.
5. Calcolare la media dei valori $g_i$ e l'incertezza associata. Valutare la riuscita o meno dell'esperimento.

**Esempio di output**:  
Un grafico con barre di errore per i dati sperimentali e una curva teorica sovrapposta.  

