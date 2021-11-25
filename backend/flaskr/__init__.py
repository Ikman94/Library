import os
from flask import Flask, json, request, abort, jsonify
from flask.globals import current_app
from flask_sqlalchemy import SQLAlchemy  # , or_
from flask_cors import CORS
import random

from models import setup_db, Book

BOOKS_PER_SHELF = 8

def paginate_books(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1)* BOOKS_PER_SHELF
    end = start + BOOKS_PER_SHELF

    books = [book.format() for book in selection] 
    current_book = books[start:end]

    return current_book
# @TODO: General Instructions
#   - As you're creating endpoints, define them and then search for 'TODO' within the frontend to update the endpoints there.
#     If you do not update the endpoints, the lab will not work - of no fault of your API code!
#   - Make sure for each route that you're thinking through when to abort and with which kind of error
#   - If you change any of the response body keys, make sure you update the frontend to correspond.


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response


    @app.route('/books')
    def get_books():
        selection = Book.query.order_by(Book.id).all()
        current_book = paginate_books(request, selection)

        if len(current_book) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'books': current_book,
            'total_books': len(Book.query.all())
        })

    @app.route('/books/<int:book_id>', methods=['PATCH'])
    def changeRating(book_id):
        body = request.get_json()
        try:
            book = Book.query.filter(Book.id==book_id).one_or_none()
            if book is None:
                abort(404)
            if 'rating' in body:
                book.rating = body['rating']
            book.update()
            return jsonify({
            'success': True,
            'id': book.id
            })
        except:
            abort(400)

    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        try:
            page = request.args.get('page', 1, type=int)
            start = (page - 1)* BOOKS_PER_SHELF
            end = start + BOOKS_PER_SHELF
            book = Book.query.filter(Book.id==book_id).first()
            if book is None:
                abort(404)
            
            book.delete()
            books = Book.query.order_by(Book.id).all()
            formatted_books = [book.format() for book in books]

            return jsonify({
            'success': True,
            "deleted": book_id,
            'books': formatted_books[start:end],
            'total_books': len(books)

            })
        except:
            abort(422)

            
    @app.route('/books', methods=['POST'])
    def createBook():
        body = request.get_json()

        title = body.get('title', None)
        author = body.get('author', None)
        rating = body.get('rating', None)
        search = body.get('search', None)

        try:
            if search:
                selection = Book.query.order_by(Book.id).filter(
                    Book.title.ilike("%{}%".format(search))
                )
                current_books =  paginate_books(request, selection)

                return jsonify({
                'success': True,
                'books': current_books,
                'total_books': len(selection.all())
                })

            else:
                book =Book(title=title, author=author, rating=rating)
                book.insert()

                selection = Book.query.order_by(Book.id).all()
                current_book = paginate_books(request, selection)
                
                return jsonify({
                'success': True,
                'created': book.id,
                'books': current_book,
                'total_books': len(Book.query.all())
                })
        except:
            abort(422)

    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not Found"
        }), 404


    @app.errorhandler(422)
    def unproccesable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400
    
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed"
        }), 405
        
    return app
