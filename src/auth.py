from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

auth = HTTPBasicAuth()

# Local user list for Demo
users = {
    "joaquim": generate_password_hash("password1"),
    "giga": generate_password_hash("password2")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username