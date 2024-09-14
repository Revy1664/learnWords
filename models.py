from config import db, app


class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(10))
	text = db.Column(db.Text)

	def __repr__(self):
		return f"{name}"
	
	
with app.app_context():
	db.create_all()
