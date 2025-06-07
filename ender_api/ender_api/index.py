from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from ender_api.models.db import db
from ender_api.models.song import Song 

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)




users = [
    {
        'name': 'Dinosaur',
        'url': 'google.com',
        'id': 1
    },
    {
        'name': 'The Mirror',
        'url': 'mirror.com',
        'id': 2
    }
]

@app.route("/songs/")
def get_songs():
    print("Endpoint Working")
    songs = Song.query.all()
    
    print(songs)
    
    return jsonify([song.to_dict() for song in songs])




#  Songs Endpoint


@app.route("/songs/<int:song_id>", methods=['GET'])
def get_song(song_id):
    
    song = next((song for song in songs if song["id"] == song_id), None)
    
    if song is None:
        abort(404, description="Song not found")
        
    return jsonify(song)


#  Users Endpoint
@app.route("/users/")
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    return jsonify(users)


# Login Endpoint
@app.route("/login/", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if username == "charlie" and password == "password":
        print("Success")
        return jsonify({"message": "Login Successful"}), 200
    else: 
        print("Failure")
        return jsonify({"message": "Invalid Credentials"}), 401

#  Cookies Endpoint
@app.route("/users")
def get_cookiers():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=['GET'])
def get_cookie(user_id):
    return jsonify(users)