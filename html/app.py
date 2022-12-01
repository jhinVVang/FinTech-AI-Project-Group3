from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/main', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin@fintech.com' or \
           request.form['password'] != 'admin':
                error = 'Invalid username or password. Please try again!'
        else:
            return render_template('main.html')
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)