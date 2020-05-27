import os
from flask import Flask, render_template, request, flash
app = Flask(__name__)

username = []
passwords = []
error = None
myfile = open("state.txt", 'r+')
for line in myfile:
    i = 1
    for word in line.split():
        if i == 1:
            username.append(word)
        else:
            passwords.append(word)
            i = i + 1
myfile.seek(0, os.SEEK_END)


@app.route('/')
def home():
    return render_template("my.html")

def do_sign_up(new_user, new_pass):
    semafor = 1
    for user in username:
        if new_user == user:
            error = 'Already exists'
            print("Exista deja un utilizator cu acest username")
            semafor = 0
    if semafor == 1:
        username.append(new_user)
        passwords.append(new_pass)
        myfile.write(new_user)
        myfile.write(" ")
        myfile.write(new_pass)
        myfile.write("\n")
        print("Utilizator creat cu succes")


@app.route('/', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        error = None
        new_user = request.form['username']
        new_pass = request.form['password']
        do_sign_up(new_user, new_pass)
        return render_template("my.html", error = error)

def init():
    print("Intru")
    with open("state.txt", 'r+') as file:
        for line in file:
            i = 1
            for word in line.split():
                if i == 1:
                    print(word)
                    username.append(word)
                else:
                    print(word)
                    passwords.append(word)
                i = i + 1

if __name__ == '__main__':
    app.run();
