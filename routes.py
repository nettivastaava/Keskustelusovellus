from app import app
from db import db
from flask import render_template, redirect, request, session
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
    
@app.route("/search")
def search():
    users=list()
    return render_template("search.html", users=users)
    
@app.route("/result")
def result():
    query = request.args["query"]
    sql = "SELECT * FROM accounts WHERE username LIKE :query"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    users = result.fetchall()
    return render_template("search.html", users=users)

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
        pip = messages.poster(id)
        blocking = mes["posted_by"]
        allow = messages.blockcheck(blocking)
        return render_template("message.html", message=mes, comments=list, count=count, allow=allow)       
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
    username = accounts.username()
    if request.method == "GET":
        if profiles.show_profile(name):
            if username == name:
                list = profiles.blocked_list()
                messages = profiles.fetch_messages(name)
                return render_template("profile.html", name=name, messages=messages, list=list)
            else:
                messages = profiles.fetch_messages(name)
                return render_template("profile.html", name=name, messages=messages)
        else:
            return render_template("error.html", cause="Invalid profile.")   
    if request.method == "POST":
        if profiles.block_user(name):
            list = profiles.blocked_list()
            messages = profiles.fetch_messages(name)
            return render_template("profile.html", name=name, messages=messages, list=list)
        else:
            list = profiles.blocked_list()
            messages = profiles.fetch_messages(name)
            return render_template("profile.html", name=name, messages=messages, list=list)
            
@app.route("/message/<int:id>/delete", methods=["GET", "DELETE"])
def delete_message(id):
    mes = messages.mes_id(id)
    mes_id = mes[1]
    acc_id = accounts.account_id()
    if acc_id == mes_id:
        messages.delete_message(id)
        return redirect("/")      
    else:
        return redirect("/")    
        


@app.route("/profiles/<name>/unblock/<int:id>", methods=["GET", "POST", "DELETE"])            
def unblock_profile(name, id):
     username=accounts.username()
     if request.method == "DELETE":
         profiles.unblock_user(id)
         list = profiles.blocked_list()
         count = profiles.messages_count(name)
         return redirect("/profiles/"+username)
     if request.method == "GET":
         if profiles.show_profile(name):
             if username == name:
                 profiles.unblock_user(id)
                 list = profiles.blocked_list()
                 count = profiles.messages_count(name)
                 return render_template("profile.html", name=name, count=count, list=list)
             
             
                 



