# Git e GitHub - Mini Tutorial

Questo file contiene una guida essenziale ai comandi e concetti di Git e GitHub necessari per lavorare con il repository del corso.

---

## Cosa sono Git e GitHub?

- **Git** è un sistema di controllo di versione che ti permette di salvare e gestire le diverse versioni del tuo codice. Ogni volta che fai un cambiamento e lo "committi", stai creando un punto di salvataggio del progetto a cui puoi tornare in futuro.

- **GitHub** è una piattaforma online che utilizza Git per ospitare e condividere repository. Ti permette di collaborare con altre persone, tenere traccia del tuo lavoro e ricevere feedback.

Nel corso useremo Git e GitHub per lavorare sugli esercizi e condividere il tuo progresso con l'insegnante.

---

## 1. Fork del Repository

Per iniziare, devi creare una copia personale del repository.

1. Vai al repository principale del corso su GitHub.
2. Clicca su **Fork** in alto a destra.
3. Questo creerà una tua copia del repository sotto il tuo account GitHub.

---

## 2. Clonare il Repository

Clonare il tuo fork ti permette di lavorare sul codice in locale o su Codespaces.

### Usare Codespaces
1. Vai al tuo repository forkato su GitHub.
2. Clicca su **Code** (pulsante verde).
3. Seleziona la scheda **Codespaces** e clicca su **Create codespace on main**.

### Usare il tuo computer
1. Nel tuo terminale, digita:
   ```bash
   git clone https://github.com/<tuo_username>/coding-course.git
2. Entra nella cartella del repository:
   ```bash
   cd coding-course
   ```
## 3. Salvare il tuo lavoro (Commit e Push)

Ogni volta che completi un esercizio o fai un cambiamento, salva i tuoi progressi.

### Passaggi:
1. Aggiungi i cambiamenti a Git:
   ```bash
   git add .
   ```

2. Salva i cambiamenti con un messaggio descrittivo:
   ```bash
   git commit -m "Messaggio descrittivo del progresso"
   ```

3. Carica i cambiamenti nel tuo repository su GitHub:
   ```bash
   git push
   ```

---

## 4. Aprire una Pull Request (PR)

Le Pull Request ti permettono di chiedere feedback sul tuo lavoro.

1. Vai al tuo repository forkato su GitHub.
2. Clicca su **Pull requests**.
3. Clicca su **New pull request**.
4. Seleziona il branch `main` del tuo fork come **base** e il branch `main` del repository principale come **compare**.
5. Inserisci un titolo e un messaggio per la PR, quindi clicca su **Create pull request**.

L'insegnante potrà esaminare il tuo codice e fornire feedback.

---

## 5. Aggiornare il tuo Fork

Per mantenere il tuo fork aggiornato con il repository principale:

1. Vai al tuo repository personale su GitHub.
2. Clicca su **Sync fork**.
3. Conferma cliccando su **Update branch**.

---

## 6. Comandi essenziali riassunti

| **Comando**                          | **Descrizione**                              |
|--------------------------------------|----------------------------------------------|
| `git clone URL`                      | Clona il repository sul tuo computer         |
| `git add .`                          | Aggiunge tutti i cambiamenti al commit       |
| `git commit -m "messaggio"`          | Salva i cambiamenti localmente con un messaggio |
| `git push`                           | Carica i cambiamenti sul tuo fork su GitHub  |
| `git pull`                           | Sincronizza il repository locale con GitHub  |

---

Buon lavoro con Git e GitHub! 🚀
