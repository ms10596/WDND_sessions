from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/login")
def login():
    email = request.args.get("email")
    password = request.args.get("password")

    if email == "mail@mail.com" and password == "123456":
        return "**#mail@mail.com__0"
    else:
        abort(401)


@app.route("/secure")
def secure_route():
    token = request.headers.get("Authorization")
    token = token.split()[1]

    if token == "**#mail@mail.com__0":
        return "very confidential data"
    else:
        abort(403)






















# def check_type(func):
#     def wrapper(*args, **kwargs):
#         print("This function name is:", func.__name__)
#         print(func.__doc__)
#         if type(args[0]) == int and type(args[1]) == int:
#             return func(*args, **kwargs)
#         else:
#           return "cannot do the operation"
#     return wrapper

# @check_type
# def add(a, b):
#     return a + b

# @check_type
# def subtract(a, b):
#     return a - b

# @check_type
# def multiply(a, b):
#     return a * b


# print(add(5, 23))