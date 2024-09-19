import models
from flask import render_template, request, redirect, url_for

from config import app, db
from models import Card


# ROUTES
@app.route("/")
def index():
    # get all the cards from database
    cards = Card.query.order_by(Card.id.asc()).all()

    return render_template("index.html", cards=cards)


@app.route("/create_card", methods=["POST", "GET"])
def create_card():

    if request.method == "POST":
        # getting data from form
        word = request.form.get("word")
        context = request.form.get("context")

        # adding user to database
        new = Card(word=word, context=context)
        db.session.add(new)
        db.session.commit()

        # redirecting to index
        return redirect("/", code=302)

    return render_template("create_card.html")


@app.route("/remove/<int:card_id>")
def delete_card(card_id: int):
    # getting card by id
    card = Card.query.get(card_id)

    # deleting card from database and applying
    db.session.delete(card)
    db.session.commit()

    # redirecting to index
    return redirect("/", code=302)


@app.route("/edit_card/<int:card_id>", methods=["POST", "GET"])
def edit_card(card_id: int):
    # getting card by id
    card = Card.query.get(card_id)

    if request.method == "POST":
        # getting data from form
        word = request.form.get("word")
        context = request.form.get("context")

        # writing edited data
        card.word = word
        card.context = context

        # applying changes
        db.session.commit()

        # redirecting to index
        return redirect("/", code=302)

    return render_template("edit_card.html", card=card)


if __name__ == "__main__":
    app.run(debug=True)
