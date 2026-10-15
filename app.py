
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home ():
    name="Pranjali"
    course="Flask"
    age=28
    return render_template("index.html", 
                           name=name,
                           course=course,
                           age=age)

if __name__ == '__main__':
    app.run(debug=True)