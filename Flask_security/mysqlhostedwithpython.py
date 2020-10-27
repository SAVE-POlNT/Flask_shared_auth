from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import app, User, db
import time
# @Author : Mehdi Yc


def init():
    getPassword = User.query.all()

    return getPassword


def getUserPassword(user, passwords):

    x = ''
    for b in passwords:
        if str(b.mail) == user:
            x = str(b.password)
            exit
    return x


def setUserData(email, login, passwords):

    new_user = User(mail=email, password=login)
    if new_user:
        db.session.add(new_user)
        db.session.commit()
    db.session.commit()
    return new_user


# print(getUserPassword("mehdidouy@gmail.com"))
# Insert  #add()
# RandomUser = User('examle@example.com','password')   #ecrypted par la suite
# db.session.add(RandomUser)
# db.session.commit()

# Delete  #delete()
# db.session.delete(RandomUser)
# db.session.commit()

# Select #query.filter().first()  #query.all() to get all users
# RandomUser = User.query.filter_by(usermail='examle@example.com').first()
#  RandomUser.password  # >output : 'password' RandomUser is None in case the mail doesn t exist in the database
