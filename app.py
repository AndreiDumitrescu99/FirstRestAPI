from flask import Flask, render_template, request, flash
app = Flask(__name__)

username = []
passwords = []

@app.route('/')
def home():
    return render_template("my.html")

def do_sign_up(new_user, new_pass):
    semafor = 1
    for user in username:
        if new_user == user:
            print("Exista deja un utilizator cu acest username")
            semafor = 0
    if semafor == 1:
        username.append(new_user)
        passwords.append(new_pass)
        print("Utilizator creat cu succes")


@app.route('/', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        new_user = request.form['username']
        new_pass = request.form['password']
        do_sign_up(new_user, new_pass)
        return render_template("my.html")


if __name__ == '__main__':
    app.run();
