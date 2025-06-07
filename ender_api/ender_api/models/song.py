from ender_api.models.db import db

class Song(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    url = db.Column(db.String(100), nullable = False)
    
    def to_dict(self):
        return {"id": self.id, "name": self.name, "url": self.url}