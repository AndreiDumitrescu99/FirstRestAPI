from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("my.html")

def do_sign_up():
    print("Interceptat")

@app.route('/', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        return do_sign_up()


if __name__ == '__main__':
    app.run();
