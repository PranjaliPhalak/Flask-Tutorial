from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    courses = [
        "Python",
        "Flask",
        "react", 
        "Django"
    ]
    student = {
        "name":"pranjali",
        "city":"Surat",
        "course":"Flask"
    }
    return render_template("index.html",courses=courses, student=student)

if __name__ == "__main__":
    app.run(debug=True)
