"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "BatmanAndSpideyShouldBeInSameUniverse"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def Homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/movies')
def movies_all():

    movies = crud.all_movies()

    return render_template('movies.html', movies=movies)

@app.route('/movie/<movie_id>')
def movie_details(movie_id):

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_detail.html', movie=movie)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
