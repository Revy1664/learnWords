from config import db, app


class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	word = db.Column(db.String(50), nullable=False)
	context = db.Column(db.Text, nullable=False)

	def __str__(self):
		return self.word
