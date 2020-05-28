import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

usernames = []
passwords = []
error = None
myfile = open("state.txt", 'r+')
global_sem = 0

for line in myfile:
    i = 1
    for word in line.split():
        if i == 1:
            usernames.append(word)
        else:
            passwords.append(word)
        i = i + 1
myfile.seek(0, os.SEEK_END)

def check_for_user(user, passd):
    for i in range(len(usernames)):
        if usernames[i] == user:
            if passwords[i] == passd:
                return 1
            else:
                return 0
    return 0

@app.route('/')
def home():
    opt_param = request.args.get("username")
    if opt_param is None:
        return render_template("my.html")
    new_user = request.args.get('username')
    password = request.args.get('password')
    if check_for_user(new_user, password) == 1:
        string = '/user/' + new_user
        return redirect(string)
    return redirect('/error')

def do_sign_up(new_user, new_pass):
    semafor = 1
    for user in usernames:
        if new_user == user:
            error = 'Already exists'
            print("Exista deja un utilizator cu acest username")
            semafor = 0
    if semafor == 1:
        usernames.append(new_user)
        passwords.append(new_pass)
        myfile.write(new_user)
        myfile.write(" ")
        myfile.write(new_pass)
        myfile.write("\n")
        print("Utilizator creat cu succes")


@app.route('/', methods=["POST"])
def sign_up():
    if request.method == 'POST':
        error = None
        new_user = request.form['username']
        new_pass = request.form['password']
        do_sign_up(new_user, new_pass)
        return render_template("my.html", error = error)

@app.route('/user/<username>', methods=["GET", "DELETE", "PUT"])
def profile(username):
    global global_sem
    if request.method == 'GET':
        if username not in usernames:
            return redirect('/')
    if request.method == 'DELETE':
        return redirect('/user/delete')
    if global_sem == 1:
        global_sem = 0
        return redirect('/error')
    return render_template("user.html", value=username)

@app.route('/error')
def error():
    return ('Wrong username or password')

def delete_user(user):
    semafor = 0
    for i in range(len(usernames)):
        if usernames[i] == user:
            passd = passwords[i]
    usernames.remove(user)
    passwords.remove(passd)
    myfile.truncate(0)
    myfile.seek(0, os.SEEK_SET)
    for i in range(len(usernames)):
        myfile.write(usernames[i])
        myfile.write(" ")
        myfile.write(passwords[i])
        myfile.write("\n")

@app.route('/user/delete/', methods=["DELETE"])
def onsuccesfuldelete():
    user = request.form['username']
    delete_user(user)
    return("I tried")

@app.route('/user/newusername', methods=["PUT"])
def onsuccesfulput():
    global global_sem
    semafor = 1
    old_user = request.form['old_username']
    new_user = request.form['new_username']
    for i in range(len(usernames)):
        if usernames[i] == new_user:
            semafor = 0
    if semafor == 1:
        for i in range(len(usernames)):
            if usernames[i] == old_user:
                usernames[i] = new_user
        myfile.truncate(0)
        myfile.seek(0, os.SEEK_SET)
        for i in range(len(usernames)):
            myfile.write(usernames[i])
            myfile.write(" ")
            myfile.write(passwords[i])
            myfile.write("\n")
        return "put_succesful"
    else:
        global_sem = 1
        return "put_unsuccesful"

if __name__ == '__main__':
    app.run();
