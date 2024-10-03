from flask_login import UserMixin, current_user
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import event

from config import db, app, bcrypt, login_manager


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True)
    _password_hash = db.Column("password_hash", db.String(256), nullable=False)
    cards: Mapped[list["Card"]] = relationship(
        "Card",
        back_populates="user",
        cascade="all, delete, save-update",
    )
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = password

    @hybrid_property
    def password_hash(self):
        return self._password_hash  # Возвращаем значение хеша

    @password_hash.setter
    def password_hash(self, new_pass):
        self._password_hash = bcrypt.generate_password_hash(new_pass).decode("utf-8")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False)
    context = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user: Mapped[User] = relationship(
        "User",
        back_populates="cards"
    )

    def __str__(self):
        return self.word


@event.listens_for(Card, "before_insert")
def set_user_id(mapper, connection, target):
    if not target.user_id:
        target.user_id = current_user.id