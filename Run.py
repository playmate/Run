import streamlit as st
import random

# Lista med 80 proteinrika, kalorisnåla rätter (endast lunch & middag)
dishes = [
    "Kyckling med broccoli", "Lax med sparris", "Tonfisksallad", "Äggvita omelett", "Grillad kalkon", "Räksallad",
    "Tofu med grönsaker", "Quinoa & kikärtor", "Spenatsallad med ägg", "Biff med zucchini", "Kikärtssoppa",
    "Kycklingwok med paprika", "Linsgryta", "Fiskgryta", "Grillad torsk med grönsaker", "Kalkonburgare",
    "Sallad med räkor och avokado", "Omelett med spenat och svamp", "Grillad kyckling med blomkålsris", "Tonfiskwrap",
    "Ägg- och spenatwrap", "Kikärtsbiffar", "Lax med citronsås och broccoli", "Grillad aubergine med halloumi", "Kycklingfajita sallad",
    "Räkor med zucchininudlar", "Grillad biff med sallad", "Tofuwok med broccoli och paprika", "Sallad med kyckling och quinoa",
    "Fisk med spenat och tomater", "Kalkongryta med grönsaker", "Äggsallad med kalkon", "Linsbiffar med grönsaker",
    "Tonfisk & avokadosallad", "Kycklinggryta med paprika", "Räkwok med grönsaker", "Spenat- och tofugryta",
    "Grillad lax med sparris", "Kalkonsallad med kikärtor", "Bönsallad med fetaost", "Kycklingwrap med sallad",
    "Fisk med citron och zucchini", "Tofuwrap med grönsaker", "Räksallad med quinoa", "Kycklingsallad med avokado",
    "Tonfisk med spenat och tomat", "Grillad kalkon med grönsaker", "Ägg- och kalkonwrap", "Linsgryta med spenat",
    "Kyckling med zucchininudlar", "Fiskgryta med tomat och paprika", "Tofuwok med spenat", "Räkor med blomkålsris",
    "Kalkon med broccoli och morot", "Tonfiskbiffar med sallad", "Kycklinggryta med svamp", "Fisk med quinoa och grönsaker",
    "Spenatsoppa med äggvita", "Tofuburgare med sallad", "Räksoppa med grönsaker", "Kyckling med paprika och lök",
    "Grillad lax med tomatsallad", "Kalkonwok med grönsaker", "Tonfisk med bönsallad", "Äggsoppa med spenat",
    "Laxburgare med sallad", "Kycklingsoppa med grönsaker", "Räkor med avokadosallad", "Tofusallad med quinoa",
    "Kalkon med zucchininudlar", "Biff med blomkålsris", "Tonfisk med tomat och paprika", "Kyckling med sparris och svamp",
    "Lax med broccoli och blomkål", "Räkwok med paprika och zucchini", "Grillad kyckling med sallad", "Tofugryta med grönsaker",
    "Kalkon med spenat och tomat", "Tonfiskwrap med sallad", "Äggomelett med grönsaker", "Kycklingsallad med bönor"
]

st.set_page_config(page_title="Proteinrik Måltidscoach", layout="wide")

st.title("🍽️ Proteinrik Måltidscoach")
st.markdown("Skapa ett veckoschema med lunch och middag som är proteinrikt och kalorisnålt.")

# Veckodagar
weekdays = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]

if st.button("Generera veckoschema"):
    st.subheader("Ditt veckoschema")
    for day in weekdays:
        lunch = random.choice(dishes)
        dinner = random.choice(dishes)
        while dinner == lunch:  # undvik samma rätt för lunch och middag
            dinner = random.choice(dishes)
        st.markdown(f"**{day}**")
        st.markdown(f"- **Lunch:** {lunch}")
        st.markdown(f"- **Middag:** {dinner}")
        st.markdown("---")
