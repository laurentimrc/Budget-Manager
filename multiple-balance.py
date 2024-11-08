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
    def __init__(self, name):
        self.name = name  # Nome del bilancio, ad es. "Personale" o "Business"
        self.transactions = []

    def add_transaction(self, amount, description, transaction_type):
        if transaction_type not in ['entrata', 'uscita']:
            raise ValueError("Tipo di transazione non valido. Usa 'entrata' o 'uscita'.")
        
        if transaction_type == 'uscita':
            amount = -abs(amount)
        
        transaction = Transaction(amount, description, transaction_type)
        self.transactions.append(transaction)

    def get_balance(self):
        total_entrate = sum(t.amount for t in self.transactions if t.amount > 0)
        total_uscite = -sum(t.amount for t in self.transactions if t.amount < 0)
        saldo_corrente = total_entrate - total_uscite
        return total_entrate, total_uscite, saldo_corrente

    def show_transactions(self):
        if not self.transactions:
            return "Nessuna transazione registrata."
        
        return "\n".join(str(t) for t in self.transactions)


class AccountManager:
    def __init__(self):
        self.budgets = {}  # Dizionario di bilanci, identificati per nome
        self.current_budget = None

    def create_budget(self, name):
        if name in self.budgets:
            raise ValueError(f"Il bilancio '{name}' esiste già.")
        
        budget = BudgetManager(name)
        self.budgets[name] = budget
        self.current_budget = budget
        print(f"Creato bilancio '{name}'.")

    def select_budget(self, name):
        if name not in self.budgets:
            raise ValueError(f"Il bilancio '{name}' non esiste.")
        
        self.current_budget = self.budgets[name]
        print(f"Bilancio '{name}' selezionato.")

    def get_current_budget(self):
        return self.current_budget

    def show_all_budgets(self):
        if not self.budgets:
            return "Nessun bilancio disponibile."
        
        output = []
        for name, budget in self.budgets.items():
            entrate, uscite, saldo = budget.get_balance()
            output.append(f"Bilancio '{name}': Entrate={entrate:.2f} EUR, Uscite={uscite:.2f} EUR, Saldo={saldo:.2f} EUR")
        return "\n".join(output)


# Esempio di utilizzo
if __name__ == "__main__":
    manager = AccountManager()

    # Creazione di bilanci multipli
    manager.create_budget("Personale")
    manager.create_budget("Business")

    # Selezioniamo il bilancio "Personale" e aggiungiamo transazioni
    manager.select_budget("Personale")
    personal_budget = manager.get_current_budget()
    personal_budget.add_transaction(1500, "Stipendio", "entrata")
    personal_budget.add_transaction(300, "Affitto", "uscita")

    # Selezioniamo il bilancio "Business" e aggiungiamo transazioni
    manager.select_budget("Business")
    business_budget = manager.get_current_budget()
    business_budget.add_transaction(5000, "Vendita prodotti", "entrata")
    business_budget.add_transaction(1200, "Materiali", "uscita")

    # Visualizziamo i dettagli di tutti i bilanci
    print("\nRiepilogo bilanci:")
    print(manager.show_all_budgets())

    # Visualizziamo le transazioni nel bilancio "Personale"
    manager.select_budget("Personale")
    print("\nTransazioni del bilancio 'Personale':")
    print(personal_budget.show_transactions())

    # Visualizziamo le transazioni nel bilancio "Business"
    manager.select_budget("Business")
    print("\nTransazioni del bilancio 'Business':")
    print(business_budget.show_transactions())
