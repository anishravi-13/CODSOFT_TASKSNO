# Task 4 - Recommendation System

## Project Overview

This project is a simple movie recommendation system developed using Python.

The system recommends movies to the user based on the movie they choose. It uses content-based filtering to find movies with similar descriptions.

## How It Works

The recommendation system follows these steps:

1. The user enters the name of a movie.
2. The movie descriptions are processed using TF-IDF.
3. Cosine similarity is used to compare the movies.
4. The movies are ranked based on their similarity.
5. The system displays the top recommended movies.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Cosine Similarity

## Features

- Simple command-line interface
- Movie-based recommendations
- Content-based filtering
- TF-IDF text processing
- Cosine similarity
- Displays multiple recommended movies
- Allows the user to search again

## How to Run

Install the required libraries:

```bash
pip install pandas scikit-learn
