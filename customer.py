from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import hashlib


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/customer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)


class Customer(db.Model):
    __tablename__ = 'customer'

    cid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    paypal = db.Column(db.String(128), nullable=False)
    caddress = db.Column(db.String(128), nullable=False)

    def json(self):

        return {
            "cid": self.cid,
            "cname": self.cname,
            "email": self.email,
            "password": self.password,
            "paypal": self.paypal,
            "caddress": self.caddress
        }


@app.route("/customer")
def get_all():
    customerlist = Customer.query.all()
    if len(customerlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "customers": [customer.json() for customer in customerlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no customers."
        }
    ), 404


@app.route("/customer/<string:email>", methods=['POST'])
def find_by_email(email):
    password = request.json.get('password', None)
    email = request.json.get('email', None)
    customer = db.session.query(Customer).filter((Customer.email == email) & (Customer.password == password)).first()
    if customer:
        result = customer.json()
        del result['password']
        return jsonify(
            {
                "code": 200,
                "data": result
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Customer not found."
        }
    ), 404


@app.route("/customer", methods=['POST'])
def create_customer():
    # cid = request.json.get('cid', None)
    cname = request.json.get('cname', None)
    password = request.json.get('password', None)
    paypal = request.json.get('paypal', None)
    caddress = request.json.get('caddress', None)
    email = request.json.get('email', None)

    customer = Customer(cname=cname, email=email, caddress=caddress)

    try:
        db.session.add(customer)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the customer. " + str(e)
            }
        ), 500

    # print(json.dumps(customer.json(), default=str)) # convert a JSON object to a string and print
    # print()

    return jsonify(
        {
            "code": 201,
            "data": customer.json()
        }
    ), 201


@app.route("/customer/<string:cid>", methods=['PUT'])
def update_customer(cid):
    customer = Customer.query.filter_by(cid=cid).first()
    if customer:
        data = request.get_json()
        if data['cname']:
            customer.cname = data['cname']
        if data['email']:
            customer.email = data['email']
        if data['paypal']:
            customer.paypal = data['paypal']
        if data['password']:
            customer.password = data['password']
        if data['caddress']:
            customer.caddress = data['caddress']
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": customer.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
               "cid": cid
            },
            "message": "Customer not found."
        }
    ), 404


@app.route("/customer/<string:cid>", methods=['DELETE'])
def delete_customer(cid):
    customer = Customer.query.filter_by(cid=cid).first()
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "cid": cid
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "cid": cid
            },
            "message": "Customer not found."
        }
    ), 404


@app.route("/customer/location/<string:cid>", methods=['GET'])
def get_cus_address(cid):
    cusaddress = Customer.query.filter_by(caddress=caddresss).first()
    if customer:
         db.session.get(customer)
         db.session.commit()
         return jsonify(
             {
                 "code": 200,
                 "data": {
                     "caddress": address
                 }
             }
         )
    return jsonify(
        {
            "code": 404,
            "data": {
                "caddress": caddress
            },
            "message": "Customer not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(port=5003, debug=True)
