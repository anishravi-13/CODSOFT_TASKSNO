import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Movie information
movies = {
    "title": [
        "Avatar",
        "Avengers: Endgame",
        "Iron Man",
        "The Dark Knight",
        "Spider-Man: No Way Home",
        "Guardians of the Galaxy",
        "Interstellar",
        "Inception",
        "Jurassic World",
        "The Matrix",
        "Black Panther",
        "Doctor Strange",
        "Thor",
        "Captain America: The Winter Soldier",
        "Star Wars: The Force Awakens"
    ],

    "description": [
        "science fiction adventure action fantasy",
        "superhero action adventure science fiction",
        "superhero action science fiction technology",
        "action crime drama superhero thriller",
        "superhero action adventure science fiction",
        "superhero science fiction action adventure comedy",
        "science fiction space adventure drama",
        "science fiction thriller action mystery dream",
        "science fiction adventure action dinosaurs",
        "science fiction action thriller technology",
        "superhero action adventure science fiction",
        "superhero fantasy action magic science fiction",
        "superhero action adventure fantasy",
        "superhero action thriller adventure",
        "science fiction adventure action space"
    ]
}


# Create a DataFrame
df = pd.DataFrame(movies)


# Convert movie descriptions into numbers
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(
    df["description"]
)


# Find similarity between movies
similarity = cosine_similarity(
    tfidf_matrix
)


def recommend_movies(movie_name, number_of_movies=5):

    movie_name = movie_name.strip().lower()

    movie_titles = df["title"].str.lower()

    matches = df[
        movie_titles.str.contains(
            movie_name,
            na=False
        )
    ]

    if matches.empty:

        print("\nMovie not found.")
        print("Please choose a movie from the list below:\n")

        for title in df["title"]:
            print("-", title)

        return


    movie_index = matches.index[0]


    similarity_scores = list(
        enumerate(
            similarity[movie_index]
        )
    )


    similarity_scores.sort(
        key=lambda x: x[1],
        reverse=True
    )


    recommendations = similarity_scores[1:number_of_movies + 1]


    print("\nRecommended Movies")
    print("------------------")


    for position, (index, score) in enumerate(
        recommendations,
        start=1
    ):

        print(
            f"{position}. {df.iloc[index]['title']}"
        )


def show_movies():

    print("\nAvailable Movies")
    print("----------------")

    for number, title in enumerate(
        df["title"],
        start=1
    ):

        print(f"{number}. {title}")


def main():

    print("\n==============================")
    print("   MOVIE RECOMMENDATION SYSTEM")
    print("==============================")

    print("\nThis system recommends movies")
    print("based on the movie you choose.")

    show_movies()


    while True:

        movie = input(
            "\nEnter a movie name: "
        )


        if movie.lower() == "exit":

            print("\nThank you for using the")
            print("Movie Recommendation System!")

            break


        recommend_movies(movie)


        again = input(
            "\nDo you want another recommendation? (y/n): "
        ).lower()


        if again != "y":

            print(
                "\nThank you for using the system!"
            )

            break


if __name__ == "__main__":
    main()
