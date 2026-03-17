import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Löpschema", layout="wide")
st.title("🏃 Löpschema generator")

# --- INPUT ---
distans = st.selectbox("Mål", ["5 km", "10 km", "21 km", "42 km"])
veckor = st.slider("Antal veckor", 4, 12, 6)
pass_per_vecka = st.slider("Pass per vecka", 2, 5, 3)

# --- GENERERA ---
if "schema" not in st.session_state:
    st.session_state.schema = None

if st.button("Generera schema"):
    def skapa_vecka(mål_km):
        pass_lista = []

        for i in range(pass_per_vecka):
            if i == pass_per_vecka - 1:
                pass_lista.append(("Långpass", f"{round(mål_km * 0.7,1)} km"))
            else:
                typ = random.choice(["Lugn", "Tempo", "Intervaller"])

                if typ == "Intervaller":
                    pass_lista.append(("Intervaller", "5 x 2 min"))
                elif typ == "Tempo":
                    pass_lista.append(("Tempo", f"{round(mål_km * 0.5,1)} km"))
                else:
                    pass_lista.append(("Lugn", f"{round(mål_km * 0.4,1)} km"))

        while len(pass_lista) < 7:
            pass_lista.insert(random.randint(0, len(pass_lista)), ("Vila", "-"))

        return pass_lista

    mål_km = int(distans.split()[0])
    st.session_state.schema = [skapa_vecka(mål_km) for _ in range(veckor)]

# --- VISA ---
if st.session_state.schema:
    dagar = ["Mån","Tis","Ons","Tor","Fre","Lör","Sön"]

    for i, vecka in enumerate(st.session_state.schema, 1):
        st.subheader(f"Vecka {i}")

        html = "<table style='width:100%;border-collapse:collapse;'>"

        # header
        html += "<tr>"
        for dag in dagar:
            html += f"<th style='border:1px solid #ccc;padding:6px'>{dag}</th>"
        html += "</tr><tr>"

        # innehåll
        for typ, info in vecka:
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

        # 🔥 STABIL RENDERING (fixar ditt problem 100%)
        components.html(html, height=120)

        # separator
        if i < len(st.session_state.schema):
            st.divider()