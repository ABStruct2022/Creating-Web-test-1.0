import flask
from flask import render_template , Flask


app  = Flask(__name__,template_folder='template' , static_folder='static')


@app.route('/') 
def home():
    return render_template('home.html')

app.run(debug=True)