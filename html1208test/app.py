from flask import Flask, flash, redirect, render_template, request, url_for, session
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/knowledge')
def knowledge():
    return render_template('knowledge.html')

@app.route('/home')
def main():
    return render_template('main.html')

@app.route('/hom')
def hom():
    return render_template('home.html')

@app.route('/main', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin@fintech.com' or \
           request.form['password'] != 'admin':
                error = 'Invalid username or password. Please try again!'
        else:
            return render_template('home.html')
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)