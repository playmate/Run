import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Run Coach", layout="wide")

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

st.title("🏃 Run Coach")

# --- INPUT ---
col1, col2, col3 = st.columns(3)

with col1:
    distans = st.selectbox("Distans", ["5 km", "10 km", "21 km", "42 km"])

with col2:
    veckor = st.slider("Veckor", 4, 16, 8)

with col3:
    pass_per_vecka = st.slider("Pass / vecka", 2, 5, 3)

mål_tid = st.text_input("🎯 Mål (t.ex. 10 km på 50 min)")

coachläge = st.toggle("🧠 Coachläge", value=True)

# --- SESSION ---
if "schema" not in st.session_state:
    st.session_state.schema = None

# --- LOGIK ---
def skapa_progression(vecka, total, mål_km):
    bas = mål_km * 0.6
    ökning = (mål_km * 1.2 - bas) * (vecka / total)
    return round(bas + ökning, 1)

def skapa_vecka(vecka, total, mål_km):
    veckovolym = skapa_progression(vecka, total, mål_km)
    
    pass_lista = []

    intervall = "6 x 2 min"
    tempo_km = round(veckovolym * 0.3,1)
    lugn_km = round(veckovolym * 0.25,1)
    långpass = round(veckovolym * 0.5,1)

    typer = [
        ("Intervaller", intervall),
        ("Tempo", f"{tempo_km} km"),
        ("Lugn", f"{lugn_km} km"),
        ("Långpass", f"{långpass} km")
    ]

    for i in range(pass_per_vecka):
        pass_lista.append(typer[i % len(typer)])

    while len(pass_lista) < 7:
        pass_lista.insert(len(pass_lista)//2, ("Vila", "-"))

    return pass_lista, veckovolym

def coach_text(vecka, total):
    if vecka < total * 0.3:
        return "Bygg grund – håll lugnt tempo."
    elif vecka < total * 0.7:
        return "Öka intensiteten – fokus på tempo."
    else:
        return "Toppa formen – minska volym, behåll fart."

# --- GENERERA ---
if st.button("✨ Generera schema", use_container_width=True):
    mål_km = int(distans.split()[0])

    data = []
    for v in range(1, veckor + 1):
        vecka_data, volym = skapa_vecka(v, veckor, mål_km)
        data.append((vecka_data, volym))

    st.session_state.schema = data

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

    for i, (vecka, volym) in enumerate(st.session_state.schema, 1):
        st.markdown(f"## Vecka {i}")

        # --- Progress ---
        st.progress(min(volym / (int(distans.split()[0]) * 1.2), 1.0))
        st.caption(f"Veckovolym: {volym} km")

        # --- Grid ---
        html = "<div style='display:grid;grid-template-columns:repeat(7,1fr);gap:10px;'>"

        for (dag, (typ, info)) in zip(dagar, vecka):
            color = colors.get(typ, "#fff")

            html += f"""
            <div>
                <div class='header'>{dag}</div>
                <div class='card' style='background:{color};'>
                    {typ}<br><span style='font-size:13px'>{info}</span>
                </div>
            </div>
            """

        html += "</div>"

        components.html(html, height=150)

        # --- Coach ---
        if coachläge:
            st.info(f"🧠 Coach: {coach_text(i, veckor)}")

        st.divider()

    # --- TOTAL SAMMANFATTNING ---
    st.markdown("## 📊 Total sammanfattning")

    total_km = sum(v for _, v in st.session_state.schema)

    st.metric("Total distans", f"{round(total_km,1)} km")

    if mål_tid:
        st.success(f"🎯 Mål: {mål_tid}")
