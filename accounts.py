from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT password, id FROM accounts WHERE username=:username;"
    result = db.session.execute(sql, {"username":username})
    account = result.fetchone()
    
    if account == None:
    	return False
    else:
        if check_password_hash(account[0],password):
            session["username"] = username
            session["account_id"] = account[1]
            return True
        else:
            return False
            
def logout():
    del session["username"]
    del session["account_id"]

def register(username,password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO accounts (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username,password)

def account_id():
    return session.get("account_id",0)
