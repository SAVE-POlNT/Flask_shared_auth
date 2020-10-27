from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
from array import array
from models import app, db, Client
import time

# @Author : Mehdi Yc

getData = Client.query.all()


def getClientData(user):

    x = []
    for b in getData:

        if str(b.Email) == user:
            x.append(str(b.Name))
            x.append(str(b.LastName))
            x.append(str(b.CurrentBalance))
            x.append(str(b.Incomes))
            x.append(str(b.Expenses))
            print(x)
        else:
            print('non')

    return x


def setClientData(email, nom, prénom, sex, balance, incomes, expenses):
    new_client = Client(Email=email, Name=nom, LastName=prénom, Sex=sex,
                        CurrentBalance=balance, Incomes=balance, Expenses=expenses)
    if new_client:
        db.session.add(new_client)
        db.session.commit()
        time.sleep(1)

    db.session.commit()
    return new_client
