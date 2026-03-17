import streamlit as st
import random

st.set_page_config(page_title="Löpschema Generator", layout="wide")
st.title("🏃 Generera löpschema")

# --- INPUT ---
with st.expander("⚙️ Inställningar", expanded=True):
    distans = st.selectbox(
        "Mål",
        ["5 km", "10 km", "Halvmaraton (21 km)", "Maraton (42 km)"]
    )

    niva = st.selectbox(
        "Nivå",
        ["Nybörjare", "Medel", "Avancerad"]
    )

    veckor = st.slider("Antal veckor", 4, 16, 8)
    dagar_per_vecka = st.slider("Pass per vecka", 2, 6, 4)

generate = st.button("Generera löpschema")

# --- LOGIK ---
def hamta_mal_km(distans):
    return {
        "5 km": 5,
        "10 km": 10,
        "Halvmaraton (21 km)": 21,
        "Maraton (42 km)": 42
    }[distans]

def skapa_vecka(vecka_nr, total_veckor, mal_km, dagar):
    progression = vecka_nr / total_veckor
    langpass = round(mal_km * (0.5 + progression * 0.8), 1)

    pass_lista = []

    typer = ["Lugn distans", "Intervaller", "Tempo"]

    for i in range(dagar):
        if i == dagar - 1:
            pass_lista.append(("Långpass", f"{langpass} km"))
        else:
            typ = random.choice(typer)

            if typ == "Intervaller":
                pass_lista.append(("Intervaller", "5 x 3 min"))
            elif typ == "Tempo":
                pass_lista.append(("Tempo", f"{round(mal_km * 0.6,1)} km"))
            else:
                pass_lista.append(("Lugn distans", f"{round(mal_km * 0.5,1)} km"))

    # fyll upp med vilodagar
    while len(pass_lista) < 7:
        pass_lista.insert(random.randint(0, len(pass_lista)), ("Vila", "-"))

    return pass_lista

# --- GENERERA ---
if generate:
    mal_km = hamta_mal_km(distans)

    dagar_namn = ["Mån","Tis","Ons","Tor","Fre","Lör","Sön"]

    for vecka in range(1, veckor + 1):
        st.subheader(f"Vecka {vecka}")

        schema = skapa_vecka(vecka, veckor, mal_km, dagar_per_vecka)

        # --- HTML TABELL ---
        html = "<table style='width:100%;border-collapse:collapse;'>"

        # header
        html += "<tr>"
        for dag in dagar_namn:
            html += f"<th style='border:1px solid #ccc;text-align:center'>{dag}</th>"
        html += "</tr>"

        # innehåll
        html += "<tr>"
        for typ, info in schema:
            if typ == "Vila":
                color = "#E0E0E0"
            elif typ == "Långpass":
                color = "#FF9999"
            elif typ == "Intervaller":
                color = "#99CCFF"
            elif typ == "Tempo":
                color = "#FFCC99"
            else:
                color = "#99FF99"

            html += f"""
            <td style='border:1px solid white;
                       background:{color};
                       text-align:center;
                       height:80px;
                       font-weight:bold;
                       color:black'>
                {typ}<br>{info}
            </td>
            """
        html += "</tr></table>"

        # ✅ RÄTT SÄTT (detta fixar ditt problem)
        st.markdown(html, unsafe_allow_html=True)

        # --- SAMMANSTÄLLNING ---
        with st.expander(f"Sammanställning vecka {vecka}", expanded=False):
            total_km = 0
            pass_count = 0

            for typ, info in schema:
                if "km" in info:
                    km = float(info.replace(" km",""))
                    total_km += km
                    pass_count += 1

            st.markdown(f"""
            **Antal pass:** {pass_count}  
            **Total distans:** {round(total_km,1)} km
            """)

        # --- separator ---
        if vecka < veckor:
            st.markdown("<hr style='border:1px solid #e0e0e0;'>", unsafe_allow_html=True)