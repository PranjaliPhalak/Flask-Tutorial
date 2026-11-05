from flask import Blueprint

users_bp = Blueprint (
    "users",
    __name__,
    url_prefix="/users"
)

@users_bp.route("/")
def users():
    return "User Page"

@users_bp.route("/Profile")
def profile():
    return "Profile Page"