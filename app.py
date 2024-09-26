import models
from flask_login import login_user, logout_user, login_required
from flask import render_template, request, redirect, url_for, flash
from flask_wtf.csrf import generate_csrf

from config import app, db, bcrypt
from models import Card, User
from forms import LoginForm, RegistrationForm, CardForm


# ROUTES
@app.route("/")
def index():
    # get all the cards from database
    cards = Card.query.order_by(Card.id.asc()).all()
    return render_template("index.html", cards=cards)


@app.route("/create_card", methods=["POST", "GET"])
@login_required
def create_card():

    form = CardForm()

    if request.method == "POST" and form.validate():
        # getting data from form
        word = form.word.data
        context = form.context.data

        # adding user to database
        new = Card(word=word, context=context)
        db.session.add(new)
        db.session.commit()

        # redirecting to index
        return redirect("/", code=302)

    return render_template("create_card.html", form=form)


@app.route("/remove/<int:card_id>")
@login_required
def delete_card(card_id: int):
    # getting card by id
    card = Card.query.get(card_id)

    # deleting card from database and applying
    db.session.delete(card)
    db.session.commit()

    # redirecting to index
    return redirect("/", code=302)


@app.route("/edit_card/<int:card_id>", methods=["POST", "GET"])
@login_required
def edit_card(card_id: int):
    # getting card by id
    card = Card.query.get(card_id)
    form = CardForm()

    if request.method == "POST" and form.validate():
        # getting data from form
        word = form.word.data
        context = form.context.data

        # writing edited data
        card.word = word
        card.context = context

        # applying changes
        db.session.commit()

        # redirecting to index
        return redirect("/", code=302)

    return render_template("edit_card.html", card=card, form=form)


@app.route("/signup", methods=["POST", "GET"])
def signup():

    form = RegistrationForm()
    if request.method == "POST" and form.validate():

        # creating a new user
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        # adding the new user to database
        db.session.add(new_user)
        db.session.commit()

        # redirect to login page after registration
        return redirect("/login", code=302)
    return render_template("signup.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():

    form = LoginForm()
    if request.method == "POST" and form.validate():

        # finding a user by entered username
        user = User.query.filter_by(username=form.username.data).first()

        # checking the entered password and hashed password
        if not user or not bcrypt.check_password_hash(user.password_hash, form.password.data):
            flash("Invalid username or password.", "error")
            return redirect("/login", code=302)

        login_user(user)
        return redirect("/", code=302)

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    # logging out the user
    logout_user()

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
