from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/product'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)


class Product(db.Model):
    __tablename__ = 'product'

    pid = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    pdescription = db.Column(db.String(128), nullable=False)
    # bizid = db.Column(db.Integer, nullable=False)

    def __init__(self, pid, pname, price, pdescription):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.pdescription = pdescription

    def json(self):
        return {"pid": self.pid, "pname": self.pname, "price": self.price, "pdescription": self.pdescription}


@app.route("/product")
def get_all():
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


@app.route("/product" ,methods=['POST'])
def create_product():
    pname = request.json.get('pname', None)
    pdesc = request.json.get('pdescription', None)
    price = request.json.get('price', None)
    
    product = Product(pname=pname,price=price,pdescription=pdesc)

    try:
        db.session.add(product)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the product. " + str(e)
            }
        ), 500
    
    print(json.dumps(produc.json(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "data": product.json()
        }
    ), 201

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
