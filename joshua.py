import csv

from cs50 import SQL

open("joflix.db", "w").close()

db = SQL("sqlite:///joflix.db")

db.execute("CREATE TABLE movies (id INTEGER, title TEXT, PRIMARY KEY(id))")

db.execute("CREATE TABLE movies_genres (only_id INTEGER, genre_id INTEGER, PRIMARY KEY(genre_id), FOREIGN KEY(only_id) REFERENCES movies(id))")

db.execute("CREATE TABLE genres (movies_id INTEGER, genre TEXT, PRIMARY KEY(movies_id), FOREIGN KEY(movies_id) REFERENCES movies_genres(genre_id))")



with open("gross movies.csv",  "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["Film"].strip().capitalize()

        id = db.execute("INSERT INTO movies (title) VALUES(?)", title)

        for genre in row["Genre"].split(", "):
            genre = genre.strip().capitalize()
            genres_id = db.execute("INSERT INTO movies_genres(only_id) VALUES((SELECT id FROM movies WHERE title =?))",title)
            db.execute("INSERT INTO genres (movies_id, genre) VALUES ((SELECT only_id FROM movies_genres WHERE only_id=?),?)" , genres_id, genre)

