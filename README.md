# Event Management System

Progetto di una web app in Django di un sistema di gestione e creazione eventi.


## Funzionalità

- Autenticazione e registrazione di utenti
- Gli utenti si dividono in due gruppi con ruoli diversi, definiti in fase di registrazione:
  - **Partecipanti**
  - **Organizzatori**
- Creazione di eventi;
- Gestione di eventi da parte degli organizzatori;
- Possibilità di vedere una scheda contatti;

## Setup

1. Clona la repository
2. Installa dipendenze:
   ```
   pip install -r requirements.txt
   ```
3. Applicazione le migrations:
   ```
   python manage.py migrate
   ```
4. Impostare gruppi di utenti e autorizzazioni:
   ```
   python manage.py setup_groups
   ```
5. (Opzionale) Creare utenti di prova:
   ```
   python manage.py setup_test_users
   ```
   Questo crea due utenti:
   - Partecipante: username `attendee`, password `attendee123`
   - Organizzatore: username `organizer`, password `organizer123`
6. Avviare il server di sviluppo:
   ```
   python manage.py runserver
   ```

## Ruoli e permessi dei vari utenti

### Partecipanti
- Sfogliare gli eventi;
- Iscriversi agli eventi;
- Disicriversi agli eventi;
- Vedere le proprie prenotazioni e annullarle;
- Vedere il numero di partecipanti agli eventi;
- Accedere alla propria area personale per vedere i dati privati.

### Organizzatori
- Hanno tutti i permessi dei partecipanti;
- Creare nuovi eventi, dalla home page, dalla sezione eventi e dall'area personale. Si può inserire il nome, la descrizione, la data, il luogo e l' ora dell'evento;
- Modificare gli eventi creati, nella sezione eventi;
- Eliminare gli eventi creati, nella sezione eventi;
- Vedere la lista dei partecipanti degli eventi creati con i loro dati personali.

## Utilizzo

1. Registrare un nuovo utente, con nome, email, password e scegliere il ruolo;
2. Effettuare il login con nome e password;
3. Sfogliare gli eventi dall'home page
4. Registrarsi ad un evento dalla sezione Prenota, inserendo il numero di telefono e l'evento
5. Vedere le proprie registrazioni dalla sezione apposita
6. Se sei un organizzatore puoi creare un nuovo evento, modificarlo, eliminarlo e vedere i dettagli dei partecipanti, nella sezione Eventi


### Dati gia creati di due utenti, per verificare il funzionamento da subito:
Organizzatore: Andrea00, andrea00@gmail.com, pass: AAAEEECCC0@
Partecipante: Mario55, mario55@gmail.com, pass: MMMPPP55@

