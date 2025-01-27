from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from database import db


class Message(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str]

    def __init__(self, message=None):
        self.message = message

    def __repr__(self):
        return f"<Message {self.message}>"
