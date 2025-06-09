from flask import Flask, jsonify, request
from flask_cors import CORS
from pathlib import Path
from ender_api.models.db import db  #
from ender_api.models.song import Song 
from ender_api.models.user import User 



app = Flask(__name__, instance_relative_config=True)

# Make sure instance folder exists
Path(app.instance_path).mkdir(parents=True, exist_ok=True)

# Define absolute path to DB inside instance folder
db_path = Path(app.instance_path) / "ender.db"

# Apply database config
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize db
db.init_app(app)

cors = CORS(app)



# users = [
#     {
#         'name': 'Dinosaur',
#         'url': 'google.com',
#         'id': 1
#     },
#     {
#         'name': 'The Mirror',
#         'url': 'mirror.com',
#         'id': 2
#     }
# ]

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
    users = User.query.all()
    
    print(users)
    
    return jsonify([user.to_dict() for user in users])

# @app.route("/users/<int:user_id>", methods=['GET'])
# def get_user(user_id):
#     return jsonify(users)


# Login Endpoint
@app.route("/login/", methods=["POST"])
def login():
    data = request.get_json()
    input_username = data.get("username")
    input_password = data.get("password")
    
    user = User.query.filter_by(username=input_username, password=input_password).first()
    

    if user:
        return jsonify({"username": input_username, "password": input_password}), 200
    else: 
        print("Failure")
        return jsonify({"message": "Invalid Credentials"}), 401

#  Cookies Endpoint
# @app.route("/users")
# def get_cookiers():
#     return jsonify(users)

# @app.route("/users/<int:user_id>", methods=['GET'])
# def get_cookie(user_id):
#     return jsonify(users)