# 🎬 AI Movie Recommendation System

An AI-powered Movie Recommendation System developed using Python and Streamlit. This application recommends movies based on user preferences such as Genre, Language, Mood, and Duration, providing an interactive and visually appealing movie recommendation experience.

---

## 🌐 Live Demo

🔗 https://srinivas-1540.streamlit.app/

---

## 📌 Project Overview

The AI Movie Recommendation System helps users discover movies that match their interests and preferences. By selecting different criteria, the system intelligently suggests the most suitable movies along with their posters, ratings, and details.

This project demonstrates the practical implementation of a recommendation system and an interactive web application using Streamlit.

---

## ✨ Features

- AI-based movie recommendations.
- Interactive and user-friendly web interface.
- Movie poster display for recommended movies.
- Recommendations based on:
  - Genre
  - Language
  - Mood
  - Duration
- Displays movie ratings and information.
- Responsive and attractive UI using Streamlit.
- Live deployment using Streamlit Community Cloud.

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pillow (PIL)
- Git & GitHub

---

## 📂 Project Structure

```
AI_Recommendation_System/

│
├── app.py
├── recommendations.py
├── movies_data.py
├── requirements.txt
├── README.md
│
└── images/
       ├── john_wick.jpg
       ├── topgun.jpg
       ├── interstellar.jpg
       ├── kgf.jpg
       ├── coco.jpg
       ├── pushpa.jpg
       ├── bahubali.jpg
       ├── inception.jpg
       ├── zootopia.jpg
       └── 3idiots.jpg
```

---

## ⚙️ How the System Works

1. Open the web application.
2. Select your preferences:
   - Genre
   - Language
   - Mood
   - Duration
3. Click the **Recommend Movies** button.
4. The recommendation engine analyzes your selections.
5. The application displays the top movie recommendations with:
   - Movie Posters
   - Ratings
   - Genre
   - Language
   - Mood
   - Duration

---

## 🚀 Installation Guide

### Clone the Repository

```bash
git clone https://github.com/srinivas-1540/AI_Recommendation_System.git
```

### Navigate to the Project Folder

```bash
cd AI_Recommendation_System
```

### Install the Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python -m streamlit run app.py
```

### Open the Application

After running the command, open:

```
http://localhost:8501
```

---

## 📋 Requirements

The project requires the following Python libraries:

```
streamlit
pillow
```

---

## 🎯 Sample Recommendation Criteria

Users can choose combinations such as:

- Action + English + Exciting + Less than 2 Hours
- Comedy + Hindi + Relaxing + More than 2 Hours
- Sci-Fi + English + Thrilling + More than 2 Hours
- Animation + English + Emotional + Less than 2 Hours

The system then recommends the most suitable movies from the dataset.

---

## 🔮 Future Enhancements

- Add a larger movie dataset.
- Integrate Machine Learning-based recommendation algorithms.
- Include OTT platform availability.
- Add search functionality.
- Allow users to rate recommended movies.
- Implement personalized user profiles and recommendations.

---

## 👨‍💻 Author

**Vardholu Srinivas**

GitHub: https://github.com/srinivas-1540

---

## 📜 License

This project is created for educational, learning, and internship purposes.