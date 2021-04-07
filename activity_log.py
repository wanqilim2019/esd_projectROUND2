#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json
import os
from os import environ
import amqp_setup


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/activity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


with app.app_context():
    db = SQLAlchemy(app)

CORS(app)

monitorBindingKey='#'


class Activity(db.Model):
    __tablename__ = 'activity'

    activity_id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    aDescription = db.Column(db.String(4000), nullable=False)
    source = db.Column(db.String(128), nullable=False)


    with app.app_context():
        def json(self):

            return {
                "activity_id": self.activity_id,
                "datetime": self.datetime,
                "aDescription": self.aDescription,
                "source" : self.source
            }

def receiveOrderLog():
    amqp_setup.check_setup()
        
    queue_name = 'Activity_Log'
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an order log by " + __file__)
    with app.app_context():
        processOrderLog(json.loads(body),__file__)
    print() # print a new line feed

def processOrderLog(order,file):
    print("Recording an order log:")
    print(order)
    print("-----------------")
    print(file)
    aDescription = order
    source = file

    activity = Activity(aDescription = aDescription, source = source)
    try:
        with app.app_context():
            db.session.add(activity)
            print(123)
            db.session.commit()
            print(321)
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while log. " + str(e)
            }
        ), 500



if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveOrderLog()
    app.run(port=5500, debug=True)
    
