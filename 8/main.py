from flask import Flask, request, abort, jsonify
from auth import verify_decode_jwt
from functools import wraps
app = Flask(__name__)

data = ["one", "two", "three", "four"]

def authenticate(permission):
    def authenticate_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                if not "Authorization" in request.headers:
                    abort(401)
                token = request.headers.get("Authorization")
                bearer, token = token.split()
                if not bearer.lower() == "bearer":
                    abort(401)
                payload = verify_decode_jwt(token)
                if not "permissions" in payload:
                    abort(403)
                if not permission in payload["permissions"]:
                    abort(403)
                # return payload
            except:
                abort(401)
            return f(*args, **kwargs)
        return wrapper
    return authenticate_decorator


@app.route("/")
@authenticate("read:data")
def index():
    return jsonify({
            "data": data
        }), 200

@app.route("/", methods=["POST"])
@authenticate("insert:data")
def add_data():
    element = request.get_json()['element']
    data.append(element)
    return jsonify({
        "data": data,
        "message": "inserted successfully"
    }), 200


