from flask_restful import Resource, reqparse
from models.author import AuthorModel

class AuthorList(Resource):
    def get(self):
        return {'authors': [author.json() for author in AuthorModel.query.all()]}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help="Name cannot be blank.")
        data = parser.parse_args()

        author = AuthorModel(name=data['name'])
        author.save_to_db()
        return author.json(), 201

class AuthorResource(Resource):
    def get(self, author_id):
        author = AuthorModel.find_by_id(author_id)
        if not author:
            return {'message': 'Author not found'}, 404
        return author.json()

    def put(self, author_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        data = parser.parse_args()

        author = AuthorModel.find_by_id(author_id)
        if author:
            author.name = data['name']
        else:
            author = AuthorModel(name=data['name'])

        author.save_to_db()
        return author.json()

    def delete(self, author_id):
        author = AuthorModel.find_by_id(author_id)
        if author:
            author.delete_from_db()
            return {'message': 'Author deleted'}
        return {'message': 'Author not found'}, 404