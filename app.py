from flask import Flask, jsonify, request, render_template
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

@app.route("/get-users", methods=["GET"])
def get_users():
    users = User.query.all()
    user_data = []
    for user in users:
        user_data.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "age": user.age
        })
    return jsonify(user_data) 

@app.route("/users1")
def users():
    users = User.query.all()
    return render_template("users.html", users=users)

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = db.get_or_404(User, id)
    return jsonify  ({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    })

@app.route("/users/<int:id>", methods=["PATCH"])
def update_user(id):
    user = db.get_or_404(User, id)
    data = request.get_json()
    if "name" in data:
        user.name = data["name"]
    if "email" in data:
        user.email = data["email"]
    if "age" in data:
        user.age = data["age"]
    db.session.commit()
    return jsonify({
        "message": "User updated successfully.",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "age": user.age
        }
    })

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = db.get_or_404(User, id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully."})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)