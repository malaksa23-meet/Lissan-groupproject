from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
 "apiKey": "AIzaSyBOufiHawoekuXi1LIGf4CfFXgneHnZeXU",
  "authDomain": "lissan-gropproject.firebaseapp.com",
  "projectId": "lissan-gropproject",
  "storageBucket": "lissan-gropproject.appspot.com",
  "messagingSenderId": "958618094477",
  "appId": "1:958618094477:web:416788c36fc8be500d4bc4",
  "measurementId": "G-TJ66BLFHJX",
  "databaseURL" :"https://lissan-gropproject-default-rtdb.europe-west1.firebasedatabase.app/"}

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()





app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/about')
def about():
    return render_template('about.html') 




@app.route('/contact')
def contact():
    return render_template('contact.html') 





@app.route('/course')
def course():
    return render_template('course.html') 


@app.route('/donate')
def donate():
    return render_template('donate.html') 

@app.route('/gallery')
def gallery():
    return render_template('gallery.html') 

@app.route('/')
def home():
    return render_template('home.html') 



@app.route('/past_projects')
def past():
    return render_template('past.html') 

@app.route('/projects')
def projects():
    return render_template('projects.html') 




@app.route('/rights')
def rights():
    return render_template('rights.html') 


@app.route('/team')
def team():
    return render_template('team.html') 

@app.route('/training')
def training():
    return render_template('training.html') 

@app.route('/updates')
def updates():
    return render_template('updates.html') 




@app.route('/women_speaking_hebrew')
def wsh():
    return render_template('wsh.html') 

@app.route('/women_speaking_hebrew_bengurion')
def wshb():
    return render_template('wshb.html') 










if __name__ == '__main__':
    app.run(debug=True,
        port = 5001)