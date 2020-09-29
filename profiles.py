from db import db
from flask import render_template, redirect, request, session
import accounts, messages, comments, likes

def show_profile(username):
    sql = "SELECT * FROM accounts WHERE username=:username;"
    result = db.session.execute(sql, {"username":username}) 
    profile = result.fetchone()
    if profile == None:
        return False
    else:
        return True
 
def messages_count(posted_by):       
    sql = "SELECT COUNT(*) FROM messages WHERE posted_by=:posted_by;"
    result =db.session.execute(sql, {"posted_by":posted_by})
    count = result.fetchone()[0]  
    return count      
    
def blocked_list():
    blocking = session["username"]
    sql = "SELECT * FROM blocks WHERE blocking=:blocking;"
    result = db.session.execute(sql, {"blocking":blocking})
    return result.fetchall() 
    
def block_user(blocked):    
    blocking = session["username"]
    sql = "SELECT * FROM blocks WHERE blocking=:blocking AND blocked=:blocked;"
    result = db.session.execute(sql, {"blocking":blocking,"blocked":blocked}) 
    test = result.fetchone()
    if test == None:
        sql = "INSERT INTO blocks (blocking, blocked) VALUES (:blocking, :blocked);"
        db.session.execute(sql, {"blocking":blocking, "blocked":blocked})
        db.session.delete(sql)
        db.session.commit()
        return True
    else:
        return False
        
def unblock_user(id):
    sql = "DELETE FROM blocks WHERE id=:id";
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True

