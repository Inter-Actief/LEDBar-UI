from sqlalchemy import Column, Integer, Text

from database import Base


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    message = Column(Text(), unique=True)

    def __init__(self, message=None):
        self.message = message

    def __repr__(self):
        return '<Message %r>' % self.message
