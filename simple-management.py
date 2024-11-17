from datetime import datetime

class Transaction:
    def __init__(self, amount, description, transaction_type):
        self.amount = amount
        self.description = description
        self.transaction_type = transaction_type  # 'entrata' o 'uscita'
        self.date = datetime.now()  # Data e ora della transazione

    def __repr__(self):
        return f"[{self.date.strftime('%Y-%m-%d %H:%M:%S')}] {self.transaction_type.capitalize()}: {self.amount:.2f} EUR - {self.description}"


class BudgetManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, description, transaction_type):
        if transaction_type not in ['entrata', 'uscita']:
            raise ValueError("Tipo di transazione non valido. Usa 'entrata' o 'uscita'.")
        
        # Se è un'uscita, rendiamo l'importo negativo
        if transaction_type == 'uscita':
            amount = -abs(amount)

        # Aggiungiamo la transazione alla lista
        transaction = Transaction(amount, description, transaction_type)
        self.transactions.append(transaction)

    def get_balance(self):
        # Calcola le entrate, le uscite e il saldo corrente
        total_entrate = sum(t.amount for t in self.transactions if t.amount > 0)
        total_uscite = -sum(t.amount for t in self.transactions if t.amount < 0)
        saldo_corrente = total_entrate - total_uscite
        return total_entrate, total_uscite, saldo_corrente

    def show_transactions(self):
        if not self.transactions:
            return "Nessuna transazione registrata."
        
        # Stampa tutte le transazioni in ordine cronologico
        return "\n".join(str(t) for t in self.transactions)


# Esempio di utilizzo
if __name__ == "__main__":
    manager = BudgetManager()

    Amount= float(input("Insert Amount\n"))
    TransactionType= input("Inserisci Type Transaction\n")
    TransactionDescription= input("Insert Description\n")

    # Aggiunta di alcune transazioni
    manager.add_transaction(Importo, TransactionDescription, TransactionType)

    # Visualizzare le transazioni
    print("Transazioni registrate:")
    print(manager.show_transactions())

    # Visualizzare il bilancio
    entrate, uscite, saldo = manager.get_balance()
    print("\nBilancio attuale:")
    print(f"Entrate totali: {entrate:.2f} EUR")
    print(f"Uscite totali: {uscite:.2f} EUR")
    print(f"Saldo corrente: {saldo:.2f} EUR")
