#!flask/bin/python
from flask import Flask, jsonify, render_template, request
import DBcm
import json

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    req = request.get_json()
    print(req)


    DBcm.addPoint(req['lat'],req['lon'],'LTE',req['carrier'])
    return "Thanks!", 200

@app.route('/show')
def get_show():
    return render_template('demo.html')


@app.route('/getpoint')
def getpoint():
    sl = DBcm.get()
    return json.dumps(sl)

@app.route('/pokritie')
def getpokritie():
    return render_template('convertcsv.json')

@app.route('/buildroute',methods=['GET'])
def buildRoute():
    point1 = request.args.get('src')
    point2 = request.args.get('dest')
    if (point1 == "Казань" and point2 == "Москва"):
         return render_template('route_test.geojson')
    return "Маршрут не построен"

if __name__ == '__main__':
    app.run(host='192.168.43.42',port=8080)

