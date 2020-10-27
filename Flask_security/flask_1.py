from flask import Flask, redirect, url_for, render_template, request, session, url_for, flash
from captchacreater import create_image_captcha
from sendmail_func import sendMail, validMail
from TokenGenerator import getTokenUser, setToken, ChangeTokenUser
from mysqlhostedwithpython import getUserPassword, setUserData, init
from MainPage import getClientData, setClientData
from flask import g
import os
import time
from datetime import timedelta
from models import app, db
from Cryptage import encode, decode


app.secret_key = os.urandom(21)
# session.permanent = True

########################################################################################


@app.route("/", methods=['GET', 'POST'])
def register():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('passw')
    prénom = request.form.get('prénom')

    if(email is not None):
        try:
            if(validMail(email)):
                if(len(password) < 8):
                    return render_template("register.html", error="Password too short please make sure it is at least 8 characters")
                else:
                    tk = setToken(email=encode(email, 11))

                    ud = setUserData(email=encode(email, 12), login=encode(
                        password, 12), passwords=init())

                    cd = setClientData(email=encode(email, 13), nom=encode(name, 13), prénom=encode(prénom, 13),
                                       sex='H', balance='0.0', incomes='0.0', expenses='0.0')
                return render_template("signin.html", wrongpassword="")
            else:
                return render_template("register.html", error="entrez un mail valide ! ")
        except:
            return render_template("register.html", error="votre mail existe deja")

    return render_template("register.html", error="")


@app.route("/account", methods=['POST'])
def account():
    tkn = request.form["token"]
    if not session.get('userMail') is None:
        z = getClientData(encode(session['userMail'], 13))
        user_tkn = str(int(getTokenUser(encode(session['userMail'], 11))))
        print("user token = "+user_tkn)
        if tkn == user_tkn:
            ChangeTokenUser(encode(session['userMail'], 11))
            return render_template("MainPage.html", name=decode(z[0], 13), firstname=decode(z[1], 13), balance=z[2], Incomes=z[3], Expenses=z[4])
        else:
            return render_template("token.html", error='error :  wrong token!')
    else:
        return redirect('/signin')


@app.route("/signin/")
def signin():
    return render_template("signin.html", wrongpassword='')


@app.route("/token", methods=['POST'])
def token():
    f = open("message.html", "r")
    ms = f.read()
    f.close()
    mail = request.form["email"]
    z = getClientData(encode(request.form["email"], 13))
    ms = str.replace(ms, "name", decode(z[0], 13))
    print(ms)
    print("coded mail : "+mail)
    print("coded mail : "+encode(mail, 11))
    print("coded mail : "+encode(mail, 12))
    print("coded mail : "+encode(mail, 13))
    session['userMail'] = mail
    password = request.form["passw"]
    print("password entred is : " + password)
    print("password is : "+decode(str(getUserPassword(encode(mail, 12), init())), 12))
    if(password == decode(str(getUserPassword(encode(mail, 12), init())), 12)):
        sendMail(mail, "Bank Token", ms)
        return render_template("token.html", error='')
    return render_template("signin.html", wrongpassword='Invalid Password Or Mail retry !')


@app.route("/resend")
def resendToken():
    f = open("./securité/message.html", "r")
    ms = f.read()
    f.close()
    sendMail(session['userMail'], "Bank Token", ms)
    return render_template("token.html")


if __name__ == "__main__":

    app.run(debug=True)
