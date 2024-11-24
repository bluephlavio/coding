# **Corso di Programmazione in Python**

## **Descrizione del Progetto**
Questo repository contiene tutto il materiale necessario per seguire il corso introduttivo di programmazione in Python progettato per studenti delle scuole superiori. Il corso guida i partecipanti attraverso i fondamenti della programmazione fino alla creazione di simulazioni avanzate, utilizzando Python e strumenti moderni come Jupyter Notebook e ipycanvas.

## **Struttura del Repository**
La struttura del repository è organizzata per garantire un facile accesso ai contenuti e un apprendimento progressivo:

- **`README.md`**: Questo file, contenente una panoramica del repository e istruzioni per iniziare.  
- **`PIANO_DEL_CORSO.md`**: Il piano dettagliato del corso, con gli obiettivi, i contenuti di ogni lezione e l’elenco degli esercizi.  
- **`GIT_AND_GITHUB_TUTORIAL.md`**: Una guida introduttiva a Git e GitHub, per aiutare gli studenti a configurare e utilizzare il repository durante il corso.  
- **`risorse/`**: Cartella contenente file condivisi tra più lezioni, come dataset o moduli Python riutilizzabili.  

---

## **Come Utilizzare Questo Repository**

### **1. Configurazione dell'Ambiente di Sviluppo**
Per iniziare, utilizzeremo **GitHub Codespaces**, un ambiente di sviluppo preconfigurato. Segui questi passaggi:
1. Forka questo repository sul tuo account GitHub.
2. Vai alla scheda **Codespaces** nel tuo repository forkato.
3. Crea un nuovo Codespace per iniziare a lavorare sul materiale del corso.

Alternativamente, puoi clonare il repository sul tuo computer locale ed eseguire il codice con Python 3.x installato.

### **2. Navigazione dei File**
- **Lezioni**: Ogni lezione ha una propria cartella (`lezione1/`, `lezione2/`, ecc.), contenente esercizi, notebook e file Python relativi.  
- **Risorse condivise**: I file comuni tra più lezioni si trovano nella cartella **`risorse/`**, come:
  - **`risorse/data.csv`**: Dataset utilizzato negli esercizi di analisi dei dati (lezione 3 e successive).  
  - **`risorse/animation.py`**: Modulo Python per gestire le animazioni, utilizzato nelle lezioni 4 e 5.

### **3. Accesso alle Risorse**
Per utilizzare i file nella cartella `risorse/`, puoi specificare un percorso relativo nei tuoi script o notebook. Ad esempio:
- Per accedere a `data.csv`:
  ```python
  import os
  import pandas as pd

  data_path = os.path.join('..', 'risorse', 'data.csv')
  data = pd.read_csv(data_path)
  ```
- Per importare `animation.py`:
  ```python
  import sys
  sys.path.append('../risorse')
  from animation import Animation
  ```

### **4. Esecuzione del Codice**
Puoi eseguire i file Python direttamente nell’ambiente Codespaces o nel tuo interprete Python locale. Per i notebook Jupyter:
1. Apri un file `.ipynb` in Codespaces o in VSCode con l'estensione appropriata.
2. Esegui le celle interattive per esplorare esempi e soluzioni.

### **5. Esercizi e Progetti**
- Gli esercizi per ogni lezione si trovano nelle rispettive sottocartelle (`lezioneX/`) e sono descritti in dettaglio nel file **PIANO_DEL_CORSO.md**.
- Gli studenti sono incoraggiati a completare gli esercizi in autonomia, utilizzando i notebook forniti per verificare il proprio lavoro.
- La lezione 5 include un progetto finale che integra le competenze acquisite durante il corso.

---

### **Domande?**
Se hai dubbi o difficoltà, non esitare a chiedere aiuto durante le lezioni o a consultare i file **PIANO_DEL_CORSO.md** e **GIT_AND_GITHUB_TUTORIAL.md**.  
Buon lavoro! 🚀  
