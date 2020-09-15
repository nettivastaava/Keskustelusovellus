from app import app
from flask import render_template, redirect, request
import accounts, messages, comments, likes, profiles

@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", messages=list)
    
@app.route("/index", methods=["GET", "POST"])
def indexi():
    return render_template("index.html")
     
@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "GET":
        return render_template("new.html")
    if request.method == "POST":
        topic = request.form["topic"]
        content = request.form["content"]
        if len(topic) > 100:
            return render_template("error.html", cause="Your title has too many characters.")
        if len(content) > 5000:
            return render_template("error.html", cause="Your message has too many characters.")
    if messages.send(topic, content):
        return redirect("/")
    else:
        return render_template("error.html", cause="Message was not. Please, try again.")
   
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if accounts.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html", cause="Invalid login credentials.")
            
@app.route("/logout", methods=["GET", "POST"])
def logout():
    accounts.logout()
    return redirect("/")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if len(username) > 25:
            return render_template("error.html", cause="Registration failed: Invalid username.")
        if accounts.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html", cause="Registration failed.")
            
@app.route("/message/<int:id>", methods=["GET", "POST"])
def message(id):
    if request.method == "GET":
        mes = messages.mes_id(id)
        list = comments.get_list(id)
        count = likes.get_likes_message(id)
        return render_template("message.html", message=mes, comments=list, count=count)       
    if request.method == "POST":
        content = request.form["content"]
        if len(content) > 5000:
            return render_template("error.html", cause="Your comment has too many characters.")
        mes = messages.mes_id(id)
        if comments.comment(content, mes):
            return redirect("/message/"+str(id))
        else:
            return render_template("error.html", cause="Your comment was not sent properly.")
           
@app.route("/message/<int:id>/like", methods=["GET", "POST"])
def like_message(id):
    mes = messages.mes_id(id)
    if likes.like_message(id):
        return redirect("/message/"+str(id))
    else:
        return redirect("/message/"+str(id))
        
@app.route("/profiles/<name>/", methods=["GET", "POST"])
def profile(name):
    if request.method == "GET":
        if profiles.show_profile(name):
            count = profiles.messages_count(name)
            return render_template("profile.html", name=name, count=count)
        else:
            return render_template("error.html", cause="Invalid profile.")   


