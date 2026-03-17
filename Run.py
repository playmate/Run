import streamlit as st
import random

# Lista med rätter
meals = [
    "Grekisk yoghurt med blåbär","Havregrynsgröt med proteinpulver","Äggviteomelett med spenat",
    "Smoothie med bär och proteinpulver","Cottage cheese med frukt","Chia pudding med mandelmjölk",
    "Äggmuffins med grönsaker","Proteinpannkakor med bär","Kvarg med nötter och kanel","Avokado och ägg på fullkornsbröd",
    "Grillad kyckling med broccoli","Lax med sparris","Torsk med blomkålsmos","Kalkonburgare med sallad",
    "Tonfisksallad med kikärtor","Räksallad med avocado","Köttfärs med zucchini-nudlar","Kycklingwok med grönsaker",
    "Quinoa med bönor och grönsaker","Grillad halloumi med grönsaker","Äggwrap med spenat","Hummus med selleri",
    "Proteinbar hemgjord","Edamamebönor","Rökt lax på gurkskivor","Tofu stir-fry","Mini omelett med grönsaker",
    "Keso med paprika och tomat","Bönsallad med örter","Kalkonskivor med gurka","Kyckling- och svampsoppa",
    "Linssoppa med grönsaker","Tonfiskröra i paprika","Grillad aubergine med halloumi","Räkor med zucchinipasta",
    "Tofu med broccoli och cashewnötter","Köttbullar i tomatsås med zucchini","Stekt torsk med spenat",
    "Kyckling- och quinoasallad","Linsgryta med tomat och paprika","Omelettwrap med lax","Råräkor med avokado",
    "Grillad kyckling med blomkålssallad","Quorn med grönsaker","Proteinshake med mandelmjölk","Spenat- och fetaomelett",
    "Sashimi med sallad","Torskburgare med spenat","Kycklingfilé med brysselkål","Räkwok med zucchini"
]

# Sätt upp Streamlit
st.set_page_config(page_title="Proteinrik Måltidscoach", layout="wide")
st.title("🥗 Proteinrik Måltidscoach")
st.subheader("Ditt veckoschema med kalorisnåla måltider")

# Generera schema
days = ["Måndag","Tisdag","Onsdag","Torsdag","Fredag","Lördag","Söndag"]
meals_per_day = 3  # frukost, lunch, middag

week_plan = {}
for day in days:
    week_plan[day] = random.sample(meals, meals_per_day)

# Visa schemat i snygga kort
for day, meal_list in week_plan.items():
    with st.container():
        st.markdown(f"### {day}")
        cols = st.columns(meals_per_day)
        for i, meal in enumerate(meal_list):
            with cols[i]:
                st.info(f"🍽️ {meal}")
