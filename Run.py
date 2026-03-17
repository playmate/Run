import streamlit as st
import random

st.set_page_config(page_title="Måltidscoach", layout="wide")

st.title("🥗 Proteinrik Måltidscoach")

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

# --- Kategorifilter ---
categories = list(set([meal["category"] for meal in meals]))
selected_categories = st.multiselect("Välj kategorier att inkludera:", categories, default=categories)

# Filtrera måltider
filtered_meals = [meal for meal in meals if meal["category"] in selected_categories]

# --- Generera veckoschema ---
if st.button("🎯 Generera veckoschema"):
    week_days = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
    schedule = {}
    for day in week_days:
        lunch = random.choice(filtered_meals)
        dinner = random.choice(filtered_meals)
        schedule[day] = {"Lunch": lunch, "Middag": dinner}
    
    st.session_state.schedule = schedule

# --- Visa veckoschema ---
if "schedule" in st.session_state:
    schedule = st.session_state.schedule
    for day, meals_for_day in schedule.items():
        st.subheader(f"📅 {day}")
        cols = st.columns(2)
        for i, (meal_type, meal) in enumerate(meals_for_day.items()):
            with cols[i]:
                st.markdown(
                    f"""
                    <div style="border-radius:10px; padding:10px; background-color:#f0f2f6; margin-bottom:10px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <strong>{meal_type}</strong><br>
                            {meal['name']}
                        </div>
                        <div>
                            <button onclick="window.location.reload()" style="background:none; border:none; cursor:pointer;">🔄</button>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )
