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

@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user and password == user.password:
        flash('Account with this email already exists. You are now logged in!')
    elif user and password != user.password:
        flash('Password is incorrect for this user.')
    else:
        crud.create_user(email, password)
        flash(f'Account for {email} created!')

    return redirect('/')


@app.route('/movies')
def movies_all():

    movies = crud.all_movies()

    return render_template('movies.html', movies=movies)

@app.route('/movie/<movie_id>')
def movie_details(movie_id):

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_detail.html', movie=movie)

@app.route('/users')
def users_all():

    users = crud.all_users()

    return render_template('users.html', users=users)

@app.route('/users/<user_id>')
def user_details(user_id):

    user = crud.get_user_by_id(user_id)

    return render_template('user_detail.html', user=user)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
