#!/usr/bin/python
from random import random
from flask import Flask, jsonify
import os
import random
import psycopg2
import json

app = Flask(__name__)

def getRecommendation():
    conn = psycopg2.connect(
        database=os.environ.get('DB_NAME','web'), user=os.environ.get('PG_USER','root'), password=os.environ.get('PG_PASS','pass'), host=os.environ.get('DB_HOST','db'), port= os.environ.get('PG_PORT','5432')
    )
#Creating a cursor object using the cursor() method
    cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
    cursor.execute("SELECT mealname, mealprice FROM meals ORDER BY RANDOM() LIMIT 1")

# Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print("Connection established to: ",data)
    return data
    # return json.dumps(data)

#Closing the connection
    conn.close()
    return data

# os.environ["API_ENDPOINT"]='meal'
# api_endpoint = os.environ.get("API_ENDPOINT")

@app.route('/')
def get_reco():
    return jsonify(getRecommendation())

if __name__ == '__main__':
    port = os.environ.get('API_PORT', 5000)
    app.run(host='0.0.0.0',port=port)
 
 #Amey Darwhekar
 