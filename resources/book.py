from flask_restful import Resource, reqparse
from models.book import BookModel

class BookList(Resource):
    def get(self):
        return {'books': [book.json() for book in BookModel.query.all()]}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True, help="Title cannot be blank.")
        parser.add_argument('author_id', type=int, required=True, help="Author ID is required.")
        data = parser.parse_args()

        book = BookModel(**data)
        book.save_to_db()
        return book.json(), 201

class BookResource(Resource):
    def get(self, book_id):
        book = BookModel.find_by_id(book_id)
        if not book:
            return {'message': 'Book not found'}, 404
        return book.json()

    def put(self, book_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('author_id', type=int, required=True)
        data = parser.parse_args()

        book = BookModel.find_by_id(book_id)
        if book:
            book.title = data['title']
            book.author_id = data['author_id']
        else:
            book = BookModel(book_id, **data)

        book.save_to_db()
        return book.json()

    def delete(self, book_id):
        book = BookModel.find_by_id(book_id)
        if book:
            book.delete_from_db()
            return {'message': 'Book deleted'}
        return {'message': 'Book not found'}, 404
