# Event Management System

Progetto di una web app in Django di un sistema di gestione e creazione eventi.


## Funzionalità

- Autenticazione e registrazione di utenti
- Gli utenti si dividono in due gruppi con ruoli diversi, definiti in fase di registrazione:
  - **Partecipanti**: 
  - **Organizzatori**
- Una scheda contatti
- Creazione di eventi
- Gestione di eventi da parte degli organizzatori

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
5. (Optional) Creare utenti di prova:
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
- Sfogliare gli eventi
- Iscriversi agli eventi
- Disicriversi agli eventi
- Vedere le proprie prenotazioni e annullarle
- Vedere il numero di partecipanti agli eventi
- Accedere alla propria area personale per vedere i dati privati

### Organizer
- Tutti i permessi dei partecipanti
- Creare nuovi eventi, dalla home page, dalla sezione eventi e dall'area personale. Si può inserire il nome, la descrizione, la data, il luogo e l' ora.
- Modificare gli eventi creati
- Eliminare gli eventi creati
- Vedere la lista dei partecipanti degli eventi creati con i loro dati personali

## Utilizzo

1. Effettuare il login con nome utente e password o registrare un nuovo utente, con nome, email, password e scegliere il ruolo.
2. Sfogliare gli eventi dall'home page
3. Registrarsi ad un evento dalla sezione Prenota, inserendo il numero di telefono e l'evento
4. Vedere le proprie registrazioni dalla sezione apposita
5. Se sei un organizzatore puoi creare un nuovo evento, modificarlo, eliminarlo e vedere i dettagli dei partecipanti, nella sezione Eventi

