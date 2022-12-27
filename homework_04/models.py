from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, deferred, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession


Base = declarative_base()
Session = sessionmaker(expire_on_commit=False, class_=AsyncSession)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True)
    email = Column(String, nullable=False)
    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    user_id = deferred(Column(Integer, ForeignKey("users.id"), nullable=False))
    user = relationship("User", back_populates="posts")
