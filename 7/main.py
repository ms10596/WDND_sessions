from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

@app.route("/secure")
def secure():
    password = request.headers["Authorization"]
    password = password.split()[1]
    
    if password == "1234":
        return {
            "secure_data": 9988736
        }
    else:
        abort(401)



# for i in range(0, 2000):
# ...     res = requests.get("http://localhost:5000/secure", headers={'Authorization': f'bearer {i}'})
# ...     if res.status_code == 200:
# ...             print(i)



























# def check_type(func):
#     def wrapper(*args, **kwargs):
#         if type(args[0]) == int and type(args[1]) == int:
#             return func(args[0], args[1])
#         else:
#             return "Please enter numbers only"
#     return wrapper


# @check_type
# def add(a, b):
#     return a +b

# @check_type
# def subtract(a, b):
#     return a - b

# @check_type
# def multiply(a, b):
#     return a * b

# print(subtract(55, 63))




















# def add(**kwargs):
#     if 'a' in kwargs and 'b' in kwargs:
#         return kwargs['a'] + kwargs['b']
#     else:
#         return "arguments are not correct"


# print(add(a=5,c=6))


# add(5,6) --> arguments (args)
# add(a=5, b=6) --> Keyword arguments (kwargs)