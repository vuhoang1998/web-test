

from flask import Flask,render_template,redirect,url_for,request
import mongoengine
from mongoengine import *

app = Flask(__name__)

#mongodb://<dbuser>:<dbpassword>@ds133328.mlab.com:33328/vuhoang98

host ="ds133328.mlab.com"
port= 33328
db_name ="vuhoang98"
user_name = "admin"
password = "141298"

mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)
class User(Document):
    yourname = StringField()
    songname = StringField()
    artists = StringField()
    image = StringField()
    link = StringField()
    email = StringField()
    password = StringField()



@app.route('/hello/', methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('form_action.html', name=name, email=email)


@app.route("/profile")
def profile():
    return render_template('profile.html')
@app.route("/music")
def music():
    return render_template("music.html",music_list= User.objects)

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


@app.route("/music-add")
def music_add():
    return render_template("music.html",music_list=User.objects)

@app.route("/register", methods=["GET","POST"])
def register():
    user =[]
    if request.method == "GET" :
        return render_template("register.html")
    elif request.method== "POST" :
        emailx = request.form["email"] #cai "email" nay la cua name
        passwordx = request.form["password"]
        #object
        user = User(email = emailx, password = passwordx ) #constructor
        user.save()


        # Validating user input

        return ("thankyou")


@app.route("/addmore",methods=["GET","POST"])
def addmore():
    if request.method =="GET" :
        return render_template("addmore.html")
    elif request.method == "POST":
        yournamex = request.form["yourname"]
        songnamex = request.form["songname"]
        artistsx = request.form["artists"]
        imagex = request.form["image"]
        linkx = request.form["link"]
        user = User(yourname = yournamex,songname= songnamex,artists= artistsx,image = imagex, link=linkx)
        user.save()
        return redirect(url_for("thankyou"))



class Food(Document):
    name = StringField()
    des = StringField()
    img = StringField()


if __name__ == '__main__':
  app.run()
