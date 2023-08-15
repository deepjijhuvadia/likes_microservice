from app import db

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    content_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Like(user_id={self.user_id}, content_id={self.content_id})"