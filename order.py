from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/order'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)


class Order(db.Model):
    __tablename__ = 'order'

    oid = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.datetime, nullable=False)
    ostatus = db.Column(db.Integer, nullable=False)
    dstatus = db.Column(db.String(128), nullable=False)
    presponse = db.Column(db.String(128), nullable=False)

    def json(self):

        return {
            "oid": self.oid,
            "quantiy": self.quantity,
            "datetime": self.datetime,
            "ostatus": self.ostatus,
            "dstatus": self.dstatus,
            "preseponse": self.presponse
        }


@app.route("/order")
def get_all():
    orderlist = order.query.all()
    if len(orderlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "order": [order.json() for order in orderlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no order."
        }
    ), 404


@app.route("/order/<string:oid>")
def find_by_oid(oid):
    order = Order.query.filter_by(oid=oid).first()
    if order:
        return jsonify(
            {
                "code": 200,
                "data": order.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "order not found."
        }
    ), 404


@app.route("/order/product/<string:pid>")
def find_by_pid(pid):
    orderlist = Product.query.filter_by(pid=pid).all()
    if len(orderlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "order": [order.json() for order in orderlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no orders."
        }
    ), 404

@app.route("/order", methods=['POST'])
def create_order():
    # oid = request.json.get('oid', None)
    quantity = request.json.get('quantity', None)
    datetime = request.json.get('pdescription', None)

    order = Order(quantity=quantity, datetime=datetime)

    try:
        db.session.add(order)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the order. " + str(e)
            }
        ), 500

    # print(json.dumps(product.json(), default=str)) # convert a JSON object to a string and print
    # print()

    return jsonify(
        {
            "code": 201,
            "data": product.json()
        }
    ), 201


@app.route("/product/<string:pid>", methods=['PUT'])
def update_product(pid):
    product = Product.query.filter_by(pid=pid).first()
    if product:
        data = request.get_json()
        if data['pname']:
            product.pname = data['pname']
        if data['price']:
            product.price = data['price']
        if data['pdescription']:
            product.pdescription = data['pdescription']
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": product.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "pid": pid
            },
            "message": "Product not found."
        }
    ), 404


@app.route("/order/<string:oid>", methods=['DELETE'])
def delete_product(oid):
    order = Order.query.filter_by(oid=oid).first()
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "oid": oid
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "oid": oid
            },
            "message": "Order not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(port=5002, debug=True)
