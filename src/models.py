from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, DateTime, func, Text, Table,Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()



class Follower(db.Model):
    __tablename__="follower"

    id:Mapped[int] = mapped_column(primary_key=True)
    user_to_id:Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    owner_user: Mapped["User"] = relationship(back_populates="followers")


class User(db.Model):
    __tablename__="user"
    id:Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    followers:Mapped[list["Follower"]] = relationship(back_populates="owner_user")
    post:Mapped["Post"] = relationship(back_populates="users")
    media:Mapped["Media"] = relationship(back_populates="owners")
    author_comment: Mapped["Comment"] = relationship(back_populates="author")
    

class Media(db.Model):
    __tablename__="media"
    id:Mapped[int] = mapped_column(primary_key=True)
    type:Mapped[int] = mapped_column(nullable=False)
    url:Mapped[str] = mapped_column(Text, nullable=False)
    post_id:Mapped[int]=mapped_column(ForeignKey("post.id"), nullable=False)
    owner:Mapped[list["Post"]]= relationship(back_populates="media")

    
class Post(db.Model):
    __tablename__="post"
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("user.id"), nullable=False)
    users:Mapped[list["User"]]= relationship(back_populates="post")
    media:Mapped["Media"]= relationship(back_populates="owner")
    post_comment:Mapped["Comment"] = relationship(back_populates="post")

class Comment(db.Model):
    __tablename__="comment"
    id:Mapped[int] = mapped_column(primary_key=True)
    comment_text:Mapped[str] = mapped_column(Text, nullable=False)
    author_id:Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    post_id:Mapped[int] = mapped_column(ForeignKey("post.id"), nullable=False)
    post:Mapped[list["Post"]] = relationship(back_populates="post_comment")
    author: Mapped[list["User"]] = relationship(back_populates="author_comment")



    
