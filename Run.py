# filnamn: meal_coach.py
import streamlit as st
import random

# Lista på proteinrika, kalorisnåla måltider
meals = [
    {"name": "Grillad kyckling med broccoli", "protein": 30, "calories": 250},
    {"name": "Tonfisksallad med spenat", "protein": 35, "calories": 220},
    {"name": "Äggvita omelett med grönsaker", "protein": 25, "calories": 180},
    {"name": "Lax med sparris", "protein": 28, "calories": 260},
    {"name": "Kikärtsgryta med paprika", "protein": 20, "calories": 200},
    {"name": "Proteinsmoothie med bär", "protein": 25, "calories": 190},
    {"name": "Grekisk yoghurt med nötter", "protein": 22, "calories": 210},
    {"name": "Räksallad med avocado", "protein": 30, "calories": 230},
]

days_of_week = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]

st.title("🥗 Måltidscoach – Veckoschema för proteinrik, kalorisnål kost")

# Knappar för att generera schema
if st.button("Generera veckoschema"):
    st.subheader("Här är ditt veckoschema:")
    for day in days_of_week:
        meal = random.choice(meals)
        st.write(f"**{day}**: {meal['name']} (Protein: {meal['protein']}g, Kalorier: {meal['calories']} kcal)")
