from db import db
from flask import session
import accounts, messages, likes

def comment(content, message):
    account_id = accounts.account_id()
    posted_by = session.get("username",0)
    message_id = message[0]
    if account_id == 0:
        return False
    sql = "INSERT INTO comments (message_id, account_id, content, posted_at, posted_by) VALUES (:message_id, :account_id, :content, NOW(), :posted_by);"
    db.session.execute(sql, {"message_id":message_id, "account_id":account_id, "content":content, "posted_by":posted_by})
    db.session.commit()
    return True
    
def get_list(message_id):
    sql = "SELECT * FROM comments WHERE message_id=:message_id;"
    result = db.session.execute(sql, {"message_id":message_id})
    return result.fetchall()
