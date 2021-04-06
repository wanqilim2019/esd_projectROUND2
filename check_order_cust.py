from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ

import requests
from invokes import invoke_http

import json

app = Flask(__name__)
CORS(app)


order_URL = environ.get('order_URL') or "http://localhost:5002/order" 
product_URL = environ.get('product_URL') or "http://localhost:5001/product" 

@app.route("/check_order_cust/<string:cid>", methods=['GET'])
def check_order_cust(cid):
    # Simple check of input format and data of the request are JSON
        # Simple check of input format and data of the request are JSON
    # do the actual work
    # 1. Send get order info
    result = processCheckOrderCust(cid)
    print('\n------------------------')
    print('\nresult: ', result)
    return jsonify(result), result["code"]


def processCheckOrderCust(cid):
    # 2. Get the order info
    # Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    order_result = invoke_http(order_URL + '/customer/' + str(cid), method='GET')
    print('order_result:', order_result)
  
    code = order_result["code"]

    if code not in range(200, 300):
        # Inform the error microservice
        print('\n\n-----Order microservice fails-----')


        # 7. Return error
        return {
            "code": 500,
            "data": {"order_result": order_result},
            "message": "Order retrival fail."
        }

    order_result_list=order_result['data']['order']
    print(order_result_list)
    product_result_list=list()
    # Invoke the shipping record microservice
    print('\n\n-----Invoking product microservice-----')

    for order in order_result_list: 
        pid=order['pid']
    
        product_result = invoke_http(
            product_URL + '/' + str(pid), method="GET")
        print("product:", product_result, '\n')
        product_result_list.append(product_result)

        # Check the shipping result;
        # if a failure, send it to the error microservice.
        code = product_result["code"]
        if code not in range(200, 300):
            # Inform the error microservice
            #print('\n\n-----Invoking error microservice as shipping fails-----')
            print('\n\n-----product error')

        else:
            # 4. confirm success
            print('\n\n-----Publishing the (product info) message-----')

    print(product_result_list)
            

    # 7. Return created order, shipping record
    return {
        "code": 201,
        "data": {
            "order_result": order_result,
            "product_result": product_result_list
        }
    }


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=5300, debug=True)
    # Notes for the parameters: 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
