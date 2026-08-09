# Task 4 - Recommendation System

## Project Description

This project is a simple **Movie Recommendation System** developed using Python.

The system recommends movies to the user based on the movie they select. It uses **content-based filtering** to identify movies with similar descriptions.

The project demonstrates how recommendation systems can use text-based features and similarity measures to provide relevant suggestions.

## Objective

The main objective of this project is to build a basic recommendation system that can:

- Accept a movie name from the user
- Analyze the movie description
- Find movies with similar content
- Recommend the most similar movies

## Technologies Used

- Python
- Pandas
- Scikit-learn

## Algorithms and Techniques

### 1. Content-Based Filtering

Content-based filtering recommends items that are similar to the item selected by the user.

In this project, movie descriptions are used as the main features for finding similar movies.

### 2. TF-IDF

TF-IDF stands for **Term Frequency-Inverse Document Frequency**.

It converts the text descriptions of movies into numerical vectors. Words that are important for a particular movie receive higher importance.

### 3. Cosine Similarity

Cosine similarity is used to measure how similar two movie descriptions are.

The similarity scores are calculated for the selected movie and the other movies. The movies with the highest scores are recommended to the user.

## How the System Works

The recommendation process follows these steps:

1. A list of movies and their descriptions is stored in a dataset.
2. The movie descriptions are processed using TF-IDF Vectorizer.
3. TF-IDF converts the descriptions into numerical vectors.
4. Cosine similarity calculates the similarity between movies.
5. The user enters the name of a movie.
6. The system finds the selected movie.
7. Similarity scores are compared.
8. The top similar movies are displayed as recommendations.

## Features

- Simple and easy-to-use interface
- Movie-based recommendations
- Content-based filtering
- TF-IDF text processing
- Cosine similarity
- Displays multiple recommendations
- Allows the user to search for another movie
- Runs directly in the Python terminal

## Installation

Make sure Python is installed on your computer.

Install the required libraries using:

```bash
pip install pandas scikit-learn
