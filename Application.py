import streamlit as st
import pandas as pd
from datetime import date

# Funzione per calcolare il saldo
def calculate_balance(dataframe):
    return dataframe["Entrate"].sum() - dataframe["Uscite"].sum()

# Configurazione iniziale della pagina
st.set_page_config(page_title="Gestione Finanze Personali", layout="centered")

# Titolo dell'app
st.title("Gestione Finanze Personali")

# Inizializzazione del database locale
if "transactions" not in st.session_state:
    st.session_state["transactions"] = pd.DataFrame(columns=["Data", "Descrizione", "Entrate", "Uscite"])

# Form per inserire una nuova transazione
with st.form("Inserisci Transazione"):
    col1, col2 = st.columns(2)
    with col1:
        date_input = st.date_input("Data", value=date.today())
        description = st.text_input("Descrizione")
    with col2:
        income = st.number_input("Entrate (€)", min_value=0.0, step=0.01, format="%.2f")
        expense = st.number_input("Uscite (€)", min_value=0.0, step=0.01, format="%.2f")
    submitted = st.form_submit_button("Aggiungi")

    if submitted:
        new_transaction = {
            "Data": date_input,
            "Descrizione": description,
            "Entrate": income,
            "Uscite": expense,
        }
        st.session_state["transactions"] = pd.concat(
            [st.session_state["transactions"], pd.DataFrame([new_transaction])],
            ignore_index=True,
        )
        st.success("Transazione aggiunta con successo!")

# Visualizzazione dei dati e del riepilogo
st.subheader("Riepilogo Transazioni")
if not st.session_state["transactions"].empty:
    st.dataframe(st.session_state["transactions"])
    saldo = calculate_balance(st.session_state["transactions"])
    st.metric(label="Saldo Totale (€)", value=f"{saldo:.2f}")
else:
    st.info("Nessuna transazione registrata.")

# Download dei dati in formato CSV
st.subheader("Esporta i Dati")
csv = st.session_state["transactions"].to_csv(index=False).encode("utf-8")
st.download_button(
    label="Scarica come CSV",
    data=csv,
    file_name="finanze_personali.csv",
    mime="text/csv",
)
