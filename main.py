from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/product'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)  



@app.route("/product")
def homepage():
    productlist = Product.query.all()
    if len(productlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "products": [product.json() for product in productlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no products."
        }
    ), 404


@app.route("/product/<string:pid>")
def find_by_pid(pid):
    product = Product.query.filter_by(pid=pid).first()
    if product:
        return jsonify(
            {
                "code": 200,
                "data": product.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Product not found."
        }
    ), 404





# @app.route("/book/<string:isbn13>", methods=['PUT'])
# def update_book(isbn13):
#     book = Book.query.filter_by(isbn13=isbn13).first()
#     if book:
#         data = request.get_json()
#         if data['title']:
#             book.title = data['title']
#         if data['price']:
#             book.price = data['price']
#         if data['availability']:
#             book.availability = data['availability'] 
#         db.session.commit()
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": book.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "data": {
#                 "isbn13": isbn13
#             },
#             "message": "Book not found."
#         }
#     ), 404


# @app.route("/book/<string:isbn13>", methods=['DELETE'])
# def delete_book(isbn13):
#     book = Book.query.filter_by(isbn13=isbn13).first()
#     if book:
#         db.session.delete(book)
#         db.session.commit()
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "isbn13": isbn13
#                 }
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "data": {
#                 "isbn13": isbn13
#             },
#             "message": "Book not found."
#         }
#     ), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)
