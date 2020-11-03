from flask import  Flask 
from flask import render_template
from flask import request,redirect,url_for

id=[0]
names=['Usuario']
surnames=['Maestro']
users=['amdin']
paswords=['admin']

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


if __name__=='__main__':
    app.run(threaded=True,debug=True,port=8000)	