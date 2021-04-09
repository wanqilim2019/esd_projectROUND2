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
    pdescription = db.Column(db.String(225), nullable=False)
    imgname = db.Column(db.String(225), nullable=False)
    bid = db.Column(db.Integer, nullable=False)
    

    def json(self):
        # self.pid = pid
        # self.pname = pname
        # self.price = price
        # self.pdescription = pdescription
        return {
            "pid": self.pid,
            "pname": self.pname, 
            "price": self.price, 
            "pdescription": self.pdescription,
            "imgname": self.imgname,
            "bid": self.bid
        }


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


@app.route("/product/business/<string:bid>")
def find_by_bid(bid):
    productlist = Product.query.filter_by(bid=bid).all()
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


@app.route("/product" ,methods=['POST'])
def create_product():
    # pid = request.json.get('pid', None)
    pname = request.json.get('pname', None)
    pdesc = request.json.get('pdescription', None)
    price = request.json.get('price', None)
    bid = request.json.get('bid', None)
    img = request.files['imgfile']
    fileext = img.filename.split('.')[-1]
    timestr = time.strftime("%Y%m%d-%H%M%S")
    imgname = str(timestr)+'.'+fileext 
    img.save(os.path.join(uploads_dir, secure_filename(imgname)))
    
    product = Product(pname=pname,price=price,pdescription=pdesc,imgname=imgname, bid=bid)

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
        if data['imgname']:
            product.imgname = data['imgname']
        if data['bid']:
            product.bid = data['bid']
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


@app.route("/product/<string:pid>", methods=['DELETE'])
def delete_product(pid):
    product = Product.query.filter_by(pid=pid).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "pid": pid
                }
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


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001, debug=True)
