# seed.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))

from ender_api.index import app  # app is safe to import now
from ender_api.models.db import db
from ender_api.models.song import Song
from ender_api.models.user import User

with app.app_context():
    db.create_all()

    if Song.query.count() == 0:
        songs = [
            {'name': 'Dinosaur', 'url': 'google.com', 'id': 1},
            {'name': 'The Mirror', 'url': 'mirror.com', 'id': 2}
        ]
        for s in songs:
            db.session.add(Song(**s))

        user = {'username': 'charlie', 'password': 'Meadowpugs99!', 'id': 1}
        db.session.add(User(**user))

        db.session.commit()
        print("✅ Database seeded")