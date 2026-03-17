import streamlit as st
import random

st.set_page_config(page_title="Måltidscoach", layout="wide", page_icon="🍽️")

st.title("🍽️ Måltidscoach - Proteinrika och kalorisnåla måltider")
st.markdown(
    """
    <style>
    /* Ändra hela appens bakgrund och text för mörk design */
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }
    .stButton>button {
        background-color:#1f6feb;
        color:white;
        border-radius:8px;
        padding:0.5em 1em;
        font-size:16px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Kategorier
categories = ["Fisk", "Kyckling", "Tofu", "Vegetariskt", "Nötter", "Ägg"]
selected_categories = st.multiselect(
    "Välj kategorier att inkludera:", 
    categories, 
    default=categories
)

# --- Lista på rätter ---
meals = [
    # Fisk
    {"name": "Lax med grönsaker", "category": "Fisk"},
    {"name": "Torsk med citron och spenat", "category": "Fisk"},
    {"name": "Tonfisk sallad", "category": "Fisk"},
    {"name": "Grillad makrill", "category": "Fisk"},
    {"name": "Sardiner på salladsbädd", "category": "Fisk"},
    {"name": "Fiskgryta med tomat", "category": "Fisk"},
    {"name": "Fisktacos med lime", "category": "Fisk"},
    {"name": "Ugnsbakad sej", "category": "Fisk"},
    {"name": "Röding med sparris", "category": "Fisk"},
    {"name": "Fiskburgare med sallad", "category": "Fisk"},

    # Kyckling
    {"name": "Grillad kyckling med broccoli", "category": "Kyckling"},
    {"name": "Kycklingwok med grönsaker", "category": "Kyckling"},
    {"name": "Kycklingsallad med quinoa", "category": "Kyckling"},
    {"name": "Kycklingfilé med zucchini", "category": "Kyckling"},
    {"name": "Kycklinggryta med paprika", "category": "Kyckling"},
    {"name": "Ugnsbakad kyckling med blomkål", "category": "Kyckling"},
    {"name": "Kycklingburgare med sallad", "category": "Kyckling"},
    {"name": "Kycklingspett med grönsaksmix", "category": "Kyckling"},
    {"name": "Kyckling i kokosmjölk", "category": "Kyckling"},
    {"name": "Kycklingwrap med grönsaker", "category": "Kyckling"},

    # Tofu
    {"name": "Stekt tofu med grönsaker", "category": "Tofu"},
    {"name": "Tofusallad med quinoa", "category": "Tofu"},
    {"name": "Tofu stir-fry med paprika", "category": "Tofu"},
    {"name": "Ugnsbakad tofu med broccoli", "category": "Tofu"},
    {"name": "Tofuwrap med hummus", "category": "Tofu"},
    {"name": "Tofugryta med kokosmjölk", "category": "Tofu"},
    {"name": "Tofuspett med grönsaksmix", "category": "Tofu"},
    {"name": "Tofu i teriyakisås", "category": "Tofu"},
    {"name": "Tofubowl med grönsaker", "category": "Tofu"},
    {"name": "Panerad tofu med sallad", "category": "Tofu"},

    # Nötkött
    {"name": "Grillad biff med sparris", "category": "Nötkött"},
    {"name": "Köttfärsbiffar med sallad", "category": "Nötkött"},
    {"name": "Biffwok med broccoli", "category": "Nötkött"},
    {"name": "Nötköttsgryta med morötter", "category": "Nötkött"},
    {"name": "Rostbiff med grönsaker", "category": "Nötkött"},
    {"name": "Nötkött och paprika stir-fry", "category": "Nötkött"},
    {"name": "Köttbullar med zucchini", "category": "Nötkött"},
    {"name": "Grillad entrecôte med sallad", "category": "Nötkött"},
    {"name": "Nötköttssallad med quinoa", "category": "Nötkött"},
    {"name": "Biffwrap med grönsaker", "category": "Nötkött"},

    # Ägg
    {"name": "Omelett med spenat och tomat", "category": "Ägg"},
    {"name": "Äggröra med broccoli", "category": "Ägg"},
    {"name": "Frittata med grönsaker", "category": "Ägg"},
    {"name": "Äggwrap med sallad", "category": "Ägg"},
    {"name": "Ägg och tonfisksallad", "category": "Ägg"},
    {"name": "Ugnsbakad äggmuffin med grönsaker", "category": "Ägg"},
    {"name": "Shakshuka med ägg", "category": "Ägg"},
    {"name": "Äggburgare med avokado", "category": "Ägg"},
    {"name": "Ägg i tomatsås", "category": "Ägg"},
    {"name": "Ägg och spenatwrap", "category": "Ägg"},

    # Vegetariskt/Övrigt
    {"name": "Quinoabowl med kikärtor", "category": "Vegetariskt"},
    {"name": "Linssallad med grönsaker", "category": "Vegetariskt"},
    {"name": "Bönburgare med sallad", "category": "Vegetariskt"},
    {"name": "Grönsakswok med tempeh", "category": "Vegetariskt"},
    {"name": "Ugnsbakad aubergine med hummus", "category": "Vegetariskt"},
    {"name": "Zucchinibiffar med sallad", "category": "Vegetariskt"},
    {"name": "Kikärtsgryta med spenat", "category": "Vegetariskt"},
    {"name": "Grönsakswrap med hummus", "category": "Vegetariskt"},
    {"name": "Tempeh stir-fry med broccoli", "category": "Vegetariskt"},
    {"name": "Ratatouille med linser", "category": "Vegetariskt"},
]

# Filtera måltider
filtered_meals = [meal for meal in meals if meal["category"] in selected_categories]

st.subheader("Generera dagsmeny")
if st.button("🎯 Generera"):
    if len(filtered_meals) < 2:
        st.warning("Välj fler kategorier eller lägg till fler rätter för att generera en meny.")
    else:
        lunch = random.choice(filtered_meals)
        dinner = random.choice([m for m in filtered_meals if m != lunch])

        # Snygga kort för mörkt tema
        st.markdown(f"""
        <div style="display:flex; gap:20px; flex-wrap:wrap;">
            <div style="flex:1; padding:20px; border-radius:15px; box-shadow:0 4px 10px rgba(0,0,0,0.5); background-color:#1e1e1e;">
                <h3 style="color:#90caf9;">Lunch 🍴</h3>
                <p style="font-size:18px; color:#e0e0e0;">{lunch['name']}</p>
                <p style="color:#b0bec5;">Kategori: {lunch['category']}</p>
            </div>
            <div style="flex:1; padding:20px; border-radius:15px; box-shadow:0 4px 10px rgba(0,0,0,0.5); background-color:#1e1e1e;">
                <h3 style="color:#f48fb1;">Middag 🍽️</h3>
                <p style="font-size:18px; color:#e0e0e0;">{dinner['name']}</p>
                <p style="color:#b0bec5;">Kategori: {dinner['category']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
