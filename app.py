from htmlpractice import read_func
from flask import Flask, render_template, request  # Import Flask

app = Flask(__name__)  # Create an app


@app.route('/')  # Define what happens at the homepage
def home():
    #return render_template("home.html")
    return "Welcome to my website"  # Send back a response

@app.route('/loginpage')  # Define what happens at the homepage
def login():
    return render_template("login.html")

@app.route('/loginsubmit', methods=['POST'])  # Define what happens at the homepage
def login_submit():
    data = request.form # retrieves form 
    name = data.get('name') 
    password = data.get('password')
    username = data.get('username')
    dob = data.get("dob") 
    try: 
        read_func("{name}", "{username}", "{password}", "{dob}", "practice.txt")
    except FileNotFoundError: 
        return"404"
if __name__ == '__main__':

    app.run(debug=True)  # Start the server
