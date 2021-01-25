from flask import Flask, request, abort, jsonify
from auth import verify_decode_jwt

from functools import wraps
app = Flask(__name__)

data = ["one", "two", "three", "four"]

def authenticate(permission=None):
    def authenticate_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            print(token)
            if not token:
                abort(401)
            bearer, token = token.split()
            
            if bearer.lower() != "bearer":
                abort(401)
            try:
                payload = verify_decode_jwt(token)
            except:
                abort(401)

            if not "permissions" in payload :
                abort(403)

            if not permission in payload["permissions"] and permission:
                abort(403)
            return f(*args, **kwargs)
        return wrapper
    return authenticate_decorator

@app.route("/")
@authenticate()
def index():
    return jsonify(data=data)

@app.route("/<element>", methods=["POST"])
@authenticate("insert:data")
def add_data(element):
    data.append(element)
    return jsonify(data=data)

