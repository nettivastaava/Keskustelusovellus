from db import db
import accounts, messages, comments

def like_message(message_id):
    account_id = accounts.account_id()
    if account_id == 0:
        return False
    else:
        sql = "SELECT id FROM likes WHERE message_id=:message_id AND account_id=:account_id;"
        result = db.session.execute(sql, {"message_id":message_id,"account_id":account_id}) 
        like = result.fetchone()
        if like == None:
              try:
                  sql = "INSERT INTO likes (message_id , account_id) VALUES (:message_id,:account_id);"
                  db.session.execute(sql, {"message_id":message_id,"account_id":account_id})
                  db.session.commit()
                  return True
              except:
                  return False 
        else:
            return False
            
def get_likes_message(message_id):
    sql = "SELECT COUNT(*) FROM likes WHERE message_id=:message_id;"
    result =db.session.execute(sql, {"message_id":message_id})
    count = result.fetchone()[0]
    if count == None:
        return 0;
    else:
        return count;
        
def like_comment(comment_id):
    account_id = accounts.account_id()
    if account_id == 0:
        return False
    else:
        sql = "SELECT id FROM likes WHERE comment_id=:comment_id AND account_id=:account_id;"
        result = db.session.execute(sql, {"comment_id":comment_id,"account_id":account_id}) 
        like = result.fetchone()
        if like == None:
              try:
                  sql = "INSERT INTO likes (comment_id , account_id) VALUES (:comment_id,:account_id);"
                  db.session.execute(sql, {"comment_id":comment_id,"account_id":account_id})
                  db.session.commit()
                  return True
              except:
                  return False 
        else:
            return False
            
def get_likes_comment(comment_id):
    sql = "SELECT COUNT(*) FROM likes WHERE comment_id=:comment_id;"
    result =db.session.execute(sql, {"comment_id":comment_id})
    count = result.fetchone()[0]   
    return count;


