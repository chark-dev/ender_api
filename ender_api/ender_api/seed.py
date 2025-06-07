from ender_api.index import app
from ender_api.models.db import db
from ender_api.models.song import Song

with app.app_context():
    db.create_all()

    if Song.query.count() == 0:
        songs = [
            {'name': 'Dinosaur', 'url': 'google.com', 'id': 1},
            {'name': 'The Mirror', 'url': 'mirror.com', 'id': 2}
        ]

        for s in songs:
            db.session.add(Song(**s))

        db.session.commit()
        print("✅ Database seeded")