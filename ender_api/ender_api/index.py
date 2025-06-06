from flask import Flask, jsonify, request, abort

app = Flask(__name__)

songs = [
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

#  Songs Endpoint
@app.route("/songs")
def get_songs():
    return jsonify(songs)

@app.route("/songs/<int:song_id>", methods=['GET'])
def get_song(song_id):
    
    song = next((song for song in songs if song["id"] == song_id), None)
    
    if song is None:
        abort(404, description="Song not found")
        
    return jsonify(song)


#  Users Endpoint
@app.route("/users")
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    return jsonify(users)

#  Cookies Endpoint
@app.route("/users")
def get_cookiers():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=['GET'])
def get_cookie(user_id):
    return jsonify(users)