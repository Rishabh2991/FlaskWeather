#from flask import Flask,request,jsonify
#import requests
#app = Flask(__name__)
#@app.route('/',methods=['GET','POST'])
#def temperature():
#	value = request.json['key']
#	return jsonify({"key" : value})
#if __name__ == '__main__':
#	app.run(debug=True)

from flask import Flask,request,jsonify
import requests
app = Flask(__name__)
#

@app.route('/<zip_c>',methods=['POST'])
def temperature(zip_c):
 zip_code = zip_c
 r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zip_code+',in&appid=d092db6ed0c1484a47477095f3aefb80')
 json_oj = r.text
 return json_oj


@app.route('/')
def index():
	return 'Hello'

if __name__ == '__main__':
	app.run(debug=True)

