#app/models.py

from app import db

# creates a database that contains the tasks submitted by the user
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    deadline = db.Column(db.String(200))

    def __repr__(self):
        return self.text
