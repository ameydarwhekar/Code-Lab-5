import requests
from flask import Flask,render_template
from flask import request
import os
import json

app = Flask(__name__)

@app.route('/')
def get_reco():
    apihost = os.environ.get('API_HOST','api')
    apiport = os.environ.get('API_PORT',5000)
    url="http://" + apihost + ":" + apiport + "/"
    r =requests.get(url)
    food_item = r.text
    food_item= food_item[1:len(food_item)-2]
    mealrec=food_item.split(",")
    return render_template('food.html',mealname=mealrec[0].replace("\"",""), mealprice=mealrec[1].replace("\"",""))
    
if __name__ == '__main__':
    port = os.environ.get('CONSUMER_PORT',81)
    app.run(host='0.0.0.0',port=port)

#Amey Darwhekar