from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('my.html')

def contact():
    if request.method == 'POST':
        if request.form['sign_up'] == 'Sign up':
            render_template('contact.html')
        else:
            pass
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run();
