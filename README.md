# Budget-Manager
A simple way to manage incomes and outcomes

## Scope and perspective
This project has the aim to simplify the finance management of a common user. The most important thing is that application must be ready to use for child.

### Spiegazione del Codice :

**Classe Transaction:** Memorizza ogni transazione con dettagli come importo, descrizione, tipo di transazione e data.
Il metodo __repr__ crea una rappresentazione leggibile della transazione.
Classe BudgetManager:

Mantiene una lista di transazioni e offre metodi per aggiungere transazioni, calcolare il bilancio e visualizzare la cronologia delle transazioni.

`add_transaction`: Aggiunge una transazione, convertendo l'importo in negativo se è un'uscita.

`get_balance`: Calcola le somme di entrate e uscite, restituendo anche il saldo corrente.

`show_transactions`: Restituisce una lista di transazioni per una visualizzazione facile.

**Esempio di utilizzo:** Alla fine, aggiungiamo alcune transazioni di esempio e mostriamo il bilancio e la cronologia.

_Questo script costituisce un buon punto di partenza per un'app di bilancio personale. Con qualche espansione, può includere persino il salvataggio dei dati in un database o file di testo.
_
### Spiegazione delle nuove classi e metodi:

`Classe AccountManager`: Dizionario budgets: Contiene tutti i bilanci, identificati da un nome univoco.
`Metodo create_budget`: Crea un nuovo bilancio (istanza di BudgetManager) e lo aggiunge al dizionario.
`Metodo select_budget`: Seleziona il bilancio attivo su cui lavorare. Assegna current_budget al bilancio selezionato.
`Metodo show_all_budgets`: Visualizza una sintesi di tutti i bilanci con entrate, uscite e saldo per ciascuno.

Modifiche alla Classe BudgetManager: Ora include un attributo name per identificare il bilancio. Utilizzo
Creiamo più bilanci (Personale e Business) e aggiungiamo transazioni specifiche a ciascuno.
Visualizziamo una sintesi di tutti i bilanci.
Mostriamo le transazioni specifiche di ciascun bilancio.
Con questa struttura, è possibile aggiungere facilmente nuove funzionalità, come il salvataggio su file o il caricamento di bilanci esistenti.
