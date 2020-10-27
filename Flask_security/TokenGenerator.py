from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
import time
from models import app, db, ConnectClient
# @Author : Mehdi Yc

getToken = ConnectClient.query.all()


def getTokenUser(user):

    x = ''
  
    for b in getToken:

        if str(b.Email) == user:
            x = str(b.Token)

    return str(int(x)-200)


def setToken(email):
    token = random.randint(1000, 9999)
    new_token = ConnectClient(Email=email, Token=token)
    if new_token:
        db.session.add(new_token)
        db.session.commit()
        time.sleep(1)

    db.session.commit()
    return new_token


def ChangeTokenUser(user):
    token = random.randint(1000, 9999)
    l_user = ConnectClient.query.filter_by(Email=user).first()
    l_user.Token = token
    db.session.commit()
    db.session.refresh(l_user)
    print(l_user)
    db.session.commit()
    # if new_token:
    #   db.session.add(new_token)
    #  db.session.commit()
    # return new_token
