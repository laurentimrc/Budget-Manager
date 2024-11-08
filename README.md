# Budget-Manager
A simple way to manage incomes &amp; outcomes

## Scope and perspective
This project has the aim to simplify the finance management of a common user. The most important thing is that application must be ready to use for child.

### Spiegazione del Codice:

Classe Transaction:

Memorizza ogni transazione con dettagli come importo, descrizione, tipo di transazione e data.
Il metodo __repr__ crea una rappresentazione leggibile della transazione.
Classe BudgetManager:

Mantiene una lista di transazioni e offre metodi per aggiungere transazioni, calcolare il bilancio e visualizzare la cronologia delle transazioni.
add_transaction: Aggiunge una transazione, convertendo l'importo in negativo se è un'uscita.
get_balance: Calcola le somme di entrate e uscite, restituendo anche il saldo corrente.
show_transactions: Restituisce una lista di transazioni per una visualizzazione facile.
Esempio di utilizzo: Alla fine, aggiungiamo alcune transazioni di esempio e mostriamo il bilancio e la cronologia.

Questo script costituisce un buon punto di partenza per un'app di bilancio personale. Con qualche espansione, può includere persino il salvataggio dei dati in un database o file di testo.
