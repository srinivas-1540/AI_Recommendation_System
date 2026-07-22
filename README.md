# AI Movie Recommendation System

## Project Description

This project is a preference-based AI movie recommendation system that suggests movies based on user interests using similarity matching logic.

## Features

- Web-based user interface
- Movie poster recommendations
- Preference-based filtering
- Match percentage calculation
- Top 3 movie recommendations
- Responsive and attractive UI

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Recommendation Logic
- Similarity Matching

## Project Structure

AI_Recommendation_System/
│
├── app.py
├── recommendations.py
├── movies_data.py
├── requirements.txt
├── README.md
├── templates/
└── static/

## How It Works

1. User selects:
   - Genre
   - Language
   - Mood
   - Duration

2. The system:
   - Compares user preferences with movie attributes.
   - Calculates a similarity score.
   - Determines a match percentage.
   - Displays the top 3 recommended movies.

## How to Run

1. Install Flask:
   pip install flask

2. Run the application:
   python app.py

3. Open:
   http://127.0.0.1:5000