from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    login = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, surname=None, login=None, email=None):
        self.name = name
        self.surname = surname
        self.login = login
        self.email = email

    def __repr__(self):
        return f'<User {self.login!r}>'
