"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')
    new_movie = crud.create_movie(movie['title'], movie['overview'],
                 release_date, movie['poster_path'])

    movies_in_db.append(new_movie)

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = f'test{n}'

    #create user
    user = crud.create_user(email, password)

    # create 10 ratings for the user
    for i in range(10):
      rand_mov = choice(movies_in_db)
      score = randint(1, 5)

      crud.create_rating(score, rand_mov.movie_id, user.user_id)
