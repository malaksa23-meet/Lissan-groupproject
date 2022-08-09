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


@app.route('/', methods=['GET', 'POST'])
def home(): 
    error = ""
    #if request.method == 'POST':
        #try:
        #login_session['user'] =auth.create_user_with_email_and_password(email, password)
        #user = {"name": name,"email":email, "password":password,"bio":bio,"user_name":user_name}
        #db.child("Users").child(login_session['user']['localId']).set(user)
        #return redirect(url_for('add_notes'))
        #except:
            #error = "Authentication failed" 
            #return render_template("signup.html", error=error)
        #return render_template("add_notes.html")
    return render_template("add_notes.html")






@app.route('/add_notes', methods=['GET', 'POST'])
def add_notes():
    error = ""
    if request.method == 'POST':
        try:
            text= request.form['text']
            title= request.form['title'] 
            note={"text":text,"title":title}
            db.child("Notes").push(note)
            all_notes=db.child("Notes").get().val()
            return redirect(url_for('all_notes'), all_notes=all_notes)
        except:
            error:"error - can't add the posts"
            return render_template("add_notes.html", error = error, all_notes=all_notes)
    else:
        all_notes=db.child("Notes").get().val()
        return render_template("add_notes.html", all_notes=all_notes)


@app.route('/sign_out', methods=['GET', 'POST'])
def sign_out():
    print('hello')
    #return render_template("")




@app.route('/delete/<string:key>', methods=['GET', 'POST'])
def delete(key):
    print("key:", key)
    db.child("Notes").child(key).remove()
    return redirect(url_for('add_notes'))


if __name__ == "__main__":
    app.run(debug=True, port = 5001)