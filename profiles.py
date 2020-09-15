from db import db
from flask import render_template, redirect, request
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
    
