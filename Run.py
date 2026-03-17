import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Löpschema PRO", layout="wide")

# --- STYLE ---
st.markdown("""
<style>
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
}
</style>
""", unsafe_allow_html=True)

st.title("🏃 Löpschema PRO")

# --- INPUT ---
col1, col2, col3 = st.columns(3)

with col1:
    distans = st.selectbox("Distans", ["5 km", "10 km", "21 km", "42 km"])

with col2:
    veckor = st.slider("Veckor", 4, 16, 8)

with col3:
    pass_per_vecka = st.slider("Pass / vecka", 2, 5, 4)

mål_tid = st.text_input("🎯 Måltid (t.ex 50 min)", "60 min")
coach = st.checkbox("🧠 Coachläge", True)

# --- SESSION ---
if "schema" not in st.session_state:
    st.session_state.schema = None

# --- LOGIK ---
def skapa_vecka(vecka, total, mål_km):
    progress = vecka / total

    # deload var 4:e vecka
    if vecka % 4 == 0:
        progress *= 0.7

    långpass = round(mål_km * (0.5 + progress * 0.6), 1)
    lugn = round(mål_km * (0.4 + progress * 0.2), 1)
    tempo = round(mål_km * (0.6 + progress * 0.2), 1)

    pass_lista = [
        ("Lugn", f"{lugn} km"),
        ("Intervaller", "6 x 2 min"),
        ("Tempo", f"{tempo} km"),
        ("Långpass", f"{långpass} km")
    ]

    # fyll upp
    while len(pass_lista) < pass_per_vecka:
        pass_lista.append(("Lugn", f"{lugn} km"))

    # vila
    while len(pass_lista) < 7:
        pass_lista.insert(random.randint(0, len(pass_lista)), ("Vila", "-"))

    return pass_lista

# --- GENERERA ---
if st.button("✨ Generera schema", use_container_width=True):
    mål_km = int(distans.split()[0])
    st.session_state.schema = [
        skapa_vecka(v, veckor, mål_km) for v in range(1, veckor+1)
    ]

# --- FÄRGER ---
colors = {
    "Vila": "#ECEFF1",
    "Långpass": "#FFCDD2",
    "Intervaller": "#BBDEFB",
    "Tempo": "#FFE0B2",
    "Lugn": "#C8E6C9"
}

dagar = ["Mån","Tis","Ons","Tor","Fre","Lör","Sön"]

# --- VISA ---
if st.session_state.schema:
    mål_km = int(distans.split()[0])

    for i, vecka in enumerate(st.session_state.schema, 1):
        st.subheader(f"Vecka {i}")

        # --- GRID ---
        html = "<div style='display:grid;grid-template-columns:repeat(7,1fr);gap:10px;'>"

        total_km = 0

        for (dag, (typ, info)) in zip(dagar, vecka):
            color = colors.get(typ)

            if "km" in info:
                total_km += float(info.replace(" km",""))

            html += f"""
            <div>
                <div class='header'>{dag}</div>
                <div class='card' style='background:{color}'>
                    {typ}<br><span style='font-size:13px'>{info}</span>
                </div>
            </div>
            """

        html += "</div>"
        components.html(html, height=150)

        # --- PROGRESS BAR ---
        max_km = mål_km * 5
        progress = min(total_km / max_km, 1.0)

        st.progress(progress, text=f"{round(total_km,1)} km denna vecka")

        # --- COACH ---
        if coach:
            if i == 1:
                st.info("Starta lugnt. Fokus på teknik och kontinuitet.")
            elif i % 4 == 0:
                st.warning("Återhämtningsvecka – ta det lugnt!")
            elif progress > 0.8:
                st.success("Bra progression! Du är nära målnivå.")
            else:
                st.info("Bygger upp volym. Håll jämnt tempo.")

        # --- SEPARATOR ---
        if i < len(st.session_state.schema):
            st.markdown("<hr style='opacity:0.2;'>", unsafe_allow_html=True)
