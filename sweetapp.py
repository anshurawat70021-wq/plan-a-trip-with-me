import streamlit as st
import random

st.set_page_config(page_title="Sweet Recipe Game 🍩", page_icon="🍰")

st.title("🍭 Sweet Treats Game 🎮")
st.write("Unlock recipes by guessing the sweet dish correctly 😋")

# ----------- RECIPES DATABASE -----------

recipes = {
    "Gulab Jamun": {
        "hint": "Round, syrupy Indian dessert 🍯",
        "ingredients": ["milk powder", "sugar", "cardamom"],
        "steps": [
            "Make dough using milk powder",
            "Shape into balls",
            "Deep fry until golden",
            "Soak in sugar syrup"
        ],
        "image": "https://source.unsplash.com/400x300/?gulab-jamun"
    },
    "Chocolate Cake": {
        "hint": "Birthday favorite 🎂",
        "ingredients": ["cocoa", "flour", "sugar"],
        "steps": [
            "Mix dry ingredients",
            "Add eggs and milk",
            "Bake in oven",
            "Decorate with frosting"
        ],
        "image": "https://source.unsplash.com/400x300/?chocolate-cake"
    },
    "Ice Cream": {
        "hint": "Cold and sweet 🍦",
        "ingredients": ["milk", "sugar", "flavor"],
        "steps": [
            "Mix ingredients",
            "Chill mixture",
            "Freeze properly",
            "Serve cold"
        ],
        "image": "https://source.unsplash.com/400x300/?ice-cream"
    },
    "Rasgulla": {
        "hint": "Soft white balls in syrup 🤍",
        "ingredients": ["paneer", "sugar", "water"],
        "steps": [
            "Make paneer balls",
            "Boil in sugar syrup",
            "Cook until fluffy",
            "Serve chilled"
        ],
        "image": "https://source.unsplash.com/400x300/?rasgulla"
    }
}

# ----------- GAME LOGIC -----------

dish = random.choice(list(recipes.keys()))

st.subheader("🔍 Guess the Sweet Dish")

st.info("Hint: " + recipes[dish]["hint"])

guess = st.text_input("Your Guess 🍬")

if st.button("Submit Guess 🎯"):
    if guess.lower() == dish.lower():
        st.success("🎉 Correct! You unlocked the recipe!")

        st.image(recipes[dish]["image"])

        st.subheader("🧾 Ingredients")
        for ing in recipes[dish]["ingredients"]:
            st.write("•", ing)

        st.subheader("👩‍🍳 Steps")
        for i, step in enumerate(recipes[dish]["steps"], 1):
            st.write(f"{i}. {step}")

        st.balloons()

    else:
        st.error("❌ Oops! Try again 😜")

# ----------- BONUS GAME -----------

st.markdown("---")
st.subheader("🔥 Bonus Round: Ingredient Guess")

dish2 = random.choice(list(recipes.keys()))
ingredient_guess = st.text_input("Guess one ingredient used in sweets 🍫")

if st.button("Check Ingredient 🧪"):
    if ingredient_guess.lower() in recipes[dish2]["ingredients"]:
        st.success("✅ Nice! That ingredient is used!")
    else:
        st.warning("😅 Not quite, try another!")

# Footer
st.markdown("---")
st.write("Made with 🍓 + 🎮 using Streamlit")
