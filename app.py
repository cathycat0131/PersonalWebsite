# from fastapi import FastAPI, Form
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse
from flask import Flask
# import uvicorn
from flask_cors import CORS
import random 

# app = FastAPI()

app = Flask(__name__)
CORS(app) 


origins = [
    "*",
    "http://ec2-18-234-86-205.compute-1.amazonaws.com/orion/"
]

user_ID_name = {}
user_name_ID = {}
unread_msg = {} # maps user_id to all their unread messages
shared_msg = {} # maps a pair of user_id and all the messages that have been opened in between them

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
@app.route('/', methods=['GET'])
def hello():
    return {'message': 'Hello, World!'}

if __name__ == '__main__':
    # uvicorn.run(app, host='0.0.0.0', port=8000)
    app.run(host='0.0.0.0', port=80)