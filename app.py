from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])  
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] 
        if username == 'test' and password == '123':
            return "<h1>Login successful!</h1>"
        else:
            return "<h1>Invalid username or password</h1>"
    return render_template('login.html')

if __name__ == '__main__':
    app.run()