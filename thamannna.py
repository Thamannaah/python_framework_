import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def rating_app():
    st.sidebar.title("Menu")
    options = ["Home", "Rating", "Results"]
    choice = st.sidebar.selectbox("Select an option", options)

    if choice == "Home":
        st.title("Welcome to product Rating Application")
        st.write("Please navigate through the menu on the left.")

    elif choice == "Rating":
        st.title("Rating")
        product_name  = st.text_input("Product Name")

        st.subheader("Ratings")
        questions = {
            "Overall Quality": ["Poor", "Average", "Good", "Excellent"],
            "Price": ["Too expensive", "Slightly expensive", "Reasonable", "Affordable"],
            "Packaging": ["Unsatisfactory", "Acceptable", "Attractive", "Luxurious"],
            "Longevity": ["Doesn't last long", "Average", "Long-lasting"],
            "Color Range": ["Limited", "Decent", "Extensive"],
            "Ease of Application": ["Difficult", "Moderate", "Easy"],
            "Skin Compatibility": ["Not suitable", "Neutral", "Suitable for all skin types"],
            "Fragrance": ["Strong", "Mild", "Fragrance-free"],
            "Texture": ["Heavy", "Smooth", "Light"],
            "Pigmentation": ["Low", "Medium", "High"]
        }
        ratings = {question: st.selectbox(question, options=questions[question]) for question in questions}

        if st.button("Submit"):
            rating_df = pd.DataFrame.from_dict(ratings, orient="index", columns=["Rating"])
            fig, ax = plt.subplots()
            ax.bar(rating_df.index, rating_df["Rating"])
            ax.set_xlabel("Aspect")
            ax.set_ylabel("Rating")
            ax.set_title("Makeup Product Ratings")
            ax.grid(True)
            plt.xticks(rotation=45)
            st.pyplot(fig)

            st.write("Product Name:", product_name)
            st.write("Ratings:")
            st.dataframe(rating_df)

    elif choice == "Results":
        st.title("Results")
        st.write("Displaying the results here.")

if __name__ == "__main__":
    rating_app()
