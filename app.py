import models
from flask import render_template, request, redirect, url_for

from config import app, db
from models import Card


# routes
@app.route("/")
def index():

	cards = Card.query.all()

	return render_template("index.html", cards=cards)

@app.route("/create_card", methods=["POST", "GET"])
def create_card():

	if request.method == "POST":
		# get data from form
		word = request.form.get("word")
		context = request.form.get("context")

		# add user to database
		new = Card(word=word, context=context)
		db.session.add(new)
		db.session.commit()

		return redirect("/", code=302)
	
	return render_template("create_card.html")

@app.route("/remove/<int:card_id>")
def delete_card(card_id: int):

	card = Card.query.get(card_id)

	db.session.delete(card)
	db.session.commit()

	return redirect("/", code=302)

@app.route("/edit_card/<int:card_id>", methods=["POST", "GET"])
def edit_card(card_id: int):

	if request.method == "POST":

		edited_word = request.form.get("word")
		edited_context = request.form.get("context")

		card = Card.query.get(card_id)

		card.word = edited_word
		card.context = edited_context

		db.session.commit()

		return redirect("/", code=302)

	return render_template("edit_card.html")

if __name__ == "__main__":
	app.run(debug=True)
