import streamlit as st
import pandas as pd

st.set_page_config(page_title="Patientenübersicht", layout="wide")
st.title("🏥 Patientenübersicht – Station M3")

# Session-State Initialisierung
if "patienten" not in st.session_state:
    st.session_state.patienten = []

# Formular zum Hinzufügen eines neuen Patienten
with st.expander("➕ Neuen Patienten hinzufügen", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
        diagnose = st.text_input("Diagnose")
        station = st.selectbox("Station", ["M3", "ZNA", "OP", "Intensiv", "andere"])
        bildgebung = st.text_input("Bildgebung (optional)")
    with col2:
        geburtsdatum = st.date_input("Geburtsdatum")
        op_termin = st.date_input("Geplanter OP-Termin", format="YYYY-MM-DD")
        vac_geplant = st.checkbox("VAC-Wechsel geplant")
        entlassung = st.date_input("Entlassdatum (geplant)", format="YYYY-MM-DD")

    if st.button("💾 Patient speichern"):
        if name.strip() and diagnose.strip():
            neuer_patient = {
                "Name": name,
                "Geburtsdatum": geburtsdatum.strftime("%d.%m.%Y"),
                "Diagnose": diagnose,
                "Station": station,
                "Bildgebung": bildgebung,
                "VAC geplant": "✅" if vac_geplant else "❌",
                "OP-Termin": op_termin.strftime("%d.%m.%Y"),
                "Entlassdatum": entlassung.strftime("%d.%m.%Y")
            }
            st.session_state.patienten.append(neuer_patient)
            st.success(f"Patient '{name}' wurde hinzugefügt.")
        else:
            st.error("Bitte Name und Diagnose angeben.")

# Anzeige der aktuellen Patientenliste
if st.session_state.patienten:
    df = pd.DataFrame(st.session_state.patienten)
    st.subheader("📋 Aktuelle Patienten")
    st.dataframe(df, use_container_width=True)
else:
    st.info("Noch keine Patienten eingetragen.")
