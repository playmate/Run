import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Löpschema", layout="wide")

# --- CSS (modern stil) ---
st.markdown("""
<style>
body {
    background-color: #f7f9fb;
}

.card {
    border-radius: 16px;
    padding: 12px;
    text-align: center;
    font-weight: 600;
    height: 90px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.header {
    font-size: 13px;
    color: #666;
    text-align:center;
    margin-bottom:4px;
}

.week {
    margin-bottom: 30px;
}

.title {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 10px;
}

.subtitle {
    color: #666;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='title'>🏃 Löpschema</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Generera ett enkelt träningsupplägg</div>", unsafe_allow_html=True)

# --- INPUT ---
col1, col2, col3 = st.columns(3)

with col1:
    distans = st.selectbox("Distans", ["5 km", "10 km", "21 km", "42 km"])

with col2:
    veckor = st.slider("Veckor", 4, 12, 6)

with col3:
    pass_per_vecka = st.slider("Pass / vecka", 2, 5, 3)

# --- SESSION ---
if "schema" not in st.session_state:
    st.session_state.schema = None

# --- GENERERA ---
if st.button("✨ Generera schema", use_container_width=True):

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

    colors = {
        "Vila": "#ECEFF1",
        "Långpass": "#FFCDD2",
        "Intervaller": "#BBDEFB",
        "Tempo": "#FFE0B2",
        "Lugn": "#C8E6C9"
    }

    for i, vecka in enumerate(st.session_state.schema, 1):
        st.markdown(f"### Vecka {i}")

        html = "<div class='week'><div style='display:grid;grid-template-columns:repeat(7,1fr);gap:10px;'>"

        for (dag, (typ, info)) in zip(dagar, vecka):
            color = colors.get(typ, "#fff")

            html += f"""
            <div>
                <div class='header'>{dag}</div>
                <div class='card' style='background:{color};'>
                    {typ}<br><span style='font-size:13px;font-weight:500'>{info}</span>
                </div>
            </div>
            """

        html += "</div></div>"

        components.html(html, height=140)

        if i < len(st.session_state.schema):
            st.markdown("<hr style='opacity:0.2;'>", unsafe_allow_html=True)