from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/users")#Static route
def users():
    return "Welcome to User Page"

@app.route("/user/<name>")#Dynamic Routes
def user(name):
    return f"Hello {name}"

@app.route("/student/<name>/<course>")#Dynamic Routes
def student(name,course):
    return f"{name} is lerning {course}"

if __name__ == "__main__":
    app.run(debug=True)
