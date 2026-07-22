# recommendations.py

from movies_data import movies


def recommend_movies(genre, language, mood, duration):

    recommendations = []

    for movie in movies:

        score = 0

        # Similarity Matching Logic

        if movie["genre"] == genre:
            score += 1

        if movie["language"] == language:
            score += 1

        if movie["mood"] == mood:
            score += 1

        if movie["duration"] == duration:
            score += 1

        # Calculate Match Percentage

        percentage = int((score / 4) * 100)

        # Assign Recommendation Labels

        if percentage == 100:
            label = "Must Watch ⭐⭐⭐⭐⭐"

        elif percentage == 75:
            label = "Highly Recommended ⭐⭐⭐⭐"

        elif percentage == 50:
            label = "Recommended ⭐⭐⭐"

        else:
            label = "Worth Trying ⭐⭐"

        # Store Movie Details Along with Match Information

        recommendations.append(
            {
                "name": movie["name"],
                "genre": movie["genre"],
                "language": movie["language"],
                "mood": movie["mood"],
                "duration": movie["duration"],
                "rating": movie["rating"],
                "image": movie["image"],
                "score": score,
                "percentage": percentage,
                "label": label,
            }
        )

    # Sort by Match Score first and Rating second

    recommendations.sort(
        key=lambda x: (x["score"], x["rating"]),
        reverse=True,
    )

    # Return Top 3 Recommended Movies

    return recommendations[:3]