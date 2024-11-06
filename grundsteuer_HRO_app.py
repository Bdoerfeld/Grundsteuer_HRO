import streamlit as st

# Titel und Einleitung
st.title("Grundsteuer-Vergleichsrechner für die Hansestadt Rostock")
st.write("""
Mit diesem Vergleichsrechner können Bürger der Hansestadt Rostock ihre bisherige Grundsteuer 
mit der ab 2025 geplanten neuen Grundsteuer vergleichen. Ziel des Rechners ist es, Transparenz zu schaffen 
und eine klare Übersicht über mögliche Veränderungen der Steuerlast zu bieten. 


""")

# Eingabe der Messbeträge
alter_messbetrag = st.number_input("Alter Grundsteuermessbetrag (Euro)", min_value=0.0, step=1.0)
neuer_messbetrag = st.number_input("Neuer Grundsteuermessbetrag (Euro)", min_value=0.0, step=1.0)

# Hebesätze für alte und neue Grundsteuer in Rostock
alter_hebesatz = 520
neuer_hebesatz = 438

# Berechnung der alten und neuen Grundsteuer
alte_grundsteuer = (alter_messbetrag * alter_hebesatz) / 100
neue_grundsteuer = (neuer_messbetrag * neuer_hebesatz) / 100

# Berechnung des erforderlichen Hebesatzes zur Aufkommensneutralität
if neuer_messbetrag > 0:
    neutral_hebesatz = (alte_grundsteuer / neuer_messbetrag) * 100
else:
    neutral_hebesatz = None

# Berechnung der Differenz zwischen neuer und alter Grundsteuer
steuer_differenz = neue_grundsteuer - alte_grundsteuer

# Anzeige der Ergebnisse
st.subheader("Ergebnisse der Grundsteuerberechnung")
st.write(f"Berechnete alte Grundsteuer: **{alte_grundsteuer:.2f} Euro**")
st.write(f"Berechnete neue Grundsteuer: **{neue_grundsteuer:.2f} Euro**")

if neutral_hebesatz is not None:
    st.write(f"Damit Ihre Grundsteuer unverändert bleibt, müsste der Hebesatz auf **{neutral_hebesatz:.2f} v.H.** festgelegt werden.")
else:
    st.write("Bitte geben Sie einen neuen Grundsteuermessbetrag ein, um den erforderlichen Hebesatz zu berechnen.")

st.write(f"Die Differenz zwischen der neuen und der alten Grundsteuer beträgt: **{steuer_differenz:.2f} Euro**")
if steuer_differenz > 0:
    st.write("Die Steuerlast wird voraussichtlich steigen.")
elif steuer_differenz < 0:
    st.write("Die Steuerlast wird voraussichtlich sinken.")
else:
    st.write("Die Steuerlast bleibt unverändert.")
