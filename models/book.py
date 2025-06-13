from db import db

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    author = db.relationship('AuthorModel')

    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id

    def json(self):
        return {'id': self.id, 'title': self.title, 'author_id': self.author_id}

    @classmethod
    def find_by_id(cls, book_id):
        return cls.query.filter_by(id=book_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
