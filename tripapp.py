import streamlit as st

# Page setup
st.set_page_config(page_title="Travel Planner ✈️", page_icon="🌍", layout="wide")

st.title("🌍 Smart Travel Planner")
st.write("Plan your dream trip (National / International) ✨")

# ----------- USER INPUT -----------

name = st.text_input("Your Name 🧳")

trip_type = st.radio("Trip Type ✈️", ["National 🇮🇳", "International 🌎"])

destination = st.text_input("Enter Destination 🌍")

days = st.slider("Number of Days 📅", 1, 15, 3)

transport = st.selectbox(
    "Choose Transport 🚗✈️",
    ["Flight ✈️", "Train 🚆", "Bus 🚌", "Car 🚗"]
)

gender = st.radio("Select Gender 👗", ["Female", "Male", "Other"])

# ----------- IMAGES (Pinterest style URLs) -----------

st.subheader("📸 Destination Inspiration")

if destination:
    st.image(f"https://source.unsplash.com/800x400/?{destination},travel")

st.subheader("🏨 Hotel Ideas")
st.image("https://source.unsplash.com/800x400/?hotel,luxury")

st.subheader("👗 Outfit Ideas")

if gender == "Female":
    st.image("https://source.unsplash.com/400x400/?women,travel,outfit")
elif gender == "Male":
    st.image("https://source.unsplash.com/400x400/?men,travel,outfit")
else:
    st.image("https://source.unsplash.com/400x400/?fashion,travel")

# ----------- LUGGAGE CHECKLIST -----------

st.subheader("🎒 Luggage Checklist")

checklist = [
    "Clothes 👕",
    "Toiletries 🪥",
    "Phone Charger 🔌",
    "ID / Passport 🪪",
    "Snacks 🍫",
    "Medicines 💊"
]

for item in checklist:
    st.checkbox(item)

# ----------- BUDGET CALCULATION -----------

st.subheader("💰 Budget Estimation")

if st.button("Calculate Budget 💸"):

    # Basic cost logic
    if transport == "Flight ✈️":
        travel_cost = 8000 if trip_type == "National 🇮🇳" else 40000
    elif transport == "Train 🚆":
        travel_cost = 2000
    elif transport == "Bus 🚌":
        travel_cost = 1500
    else:
        travel_cost = 3000

    hotel_cost_per_day = 2000 if trip_type == "National 🇮🇳" else 5000
    food_cost_per_day = 800

    total_cost = travel_cost + (hotel_cost_per_day * days) + (food_cost_per_day * days)

    st.success(f"✨ {name}, your estimated budget is ₹{total_cost}")

    st.info("💡 Tip: Always keep extra 20% budget for emergencies!")

# ----------- FOOTER -----------

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
