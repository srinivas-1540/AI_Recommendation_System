from flask import Flask, render_template, request
from recommendations import recommend_movies

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    genre = request.form["genre"]
    language = request.form["language"]
    mood = request.form["mood"]
    duration = request.form["duration"]

    movies = recommend_movies(
        genre,
        language,
        mood,
        duration
    )

    return render_template(
        "result.html",
        movies=movies
    )


if __name__ == "__main__":
    app.run(debug=True)