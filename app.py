from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///app.db"

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable= False)
    email= db.Column(db.String(120),nullable= False)
    age= db.Column(db.Integer)

@app.route("/")
def home():
    return "Flask + SQLite + SQLAlchemy is working !"

@app.route("/create-user", methods=["POST"])
def create_user():
    # user = User(
    #     name="Hitesh",
    #     email="hitesh@example.com",
    #     age=30
    # )
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    age = data.get("age")   

    user = User(
        name=name,
        email=email,
        age=age
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully.",
                    "user_id": user.id})
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # user = User(
        #     name=" Pranjal",
        #     email="pranjal@example.com",
        #     age=25
        # )
        # db.session.add(user)
        # db.session.commit()
        # print("User created successfully.")
    app.run(debug=True)