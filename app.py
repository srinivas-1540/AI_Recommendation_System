import streamlit as st
from PIL import Image
from recommendations import recommend_movies


# Page Configuration
st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Title
st.title("🎬 AI Movie Recommendation System")
st.markdown("### Find Your Perfect Movie Instantly!")

st.markdown("---")


# User Input Section
genre = st.selectbox(
    "Select Genre",
    ["Action", "Adventure", "Animation", "Comedy", "Sci-Fi"]
)

language = st.selectbox(
    "Select Language",
    ["English", "Hindi", "Telugu"]
)

mood = st.selectbox(
    "Select Mood",
    ["Exciting", "Thrilling", "Motivational", "Emotional", "Relaxing"]
)

duration = st.selectbox(
    "Select Duration",
    ["Less than 2 Hours", "More than 2 Hours"]
)


# Recommendation Button
if st.button("Recommend Movies"):

    movies = recommend_movies(
        genre,
        language,
        mood,
        duration
    )

    st.success("Your AI has found the best movie recommendations for you!")

    st.markdown("---")
    st.subheader("Top Movie Recommendations")

    # Create three columns
    cols = st.columns(3)

    for index, movie in enumerate(movies):

        if index < 3:

            with cols[index]:

                # Open Movie Poster
                image_path = f"images/{movie['image']}"
                image = Image.open(image_path)

                # Display Poster
                st.image(image, use_container_width=True)

                # Movie Details
                st.markdown(f"### {movie['name']}")
                st.write(f"⭐ Rating : {movie['rating']}/10")
                st.write(f"🎭 Genre : {movie['genre']}")
                st.write(f"🗣️ Language : {movie['language']}")
                st.write(f"😊 Mood : {movie['mood']}")
                st.write(f"⏰ Duration : {movie['duration']}")

                # Optional fields
                if "percentage" in movie:
                    st.write(f"🎯 Match Score : {movie['percentage']}%")

                if "label" in movie:
                    st.write(f"🏷️ {movie['label']}")