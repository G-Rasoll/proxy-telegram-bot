import mysql.connector
import pymysql

def CreateUser(firstname,username,lastname,user_id,languagecode,date):
    con = pymysql.Connect(host ="localhost",user = "USERNAME",passwd="",database="NAMEDATABASE")
    cs = con.cursor()

#Search to the database
    com = "SELECT * from users WHERE user_id = %s"
    vel = (user_id)
    cs.execute(com,vel)
    r = cs.fetchall()
#Add user to the database
    if r ==():
        print('تو دیتابیس نیست میرم اضافه کنم')
        com = "INSERT INTO users (firstname,lastname,username,user_id,languagecode,date_started) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (firstname,lastname,username,user_id,languagecode,date)
        try:
            cs.execute(com,val)
            con.commit()  
        except:
            print('error!')
            con.rollback()
    
        con.close()


def Support_bot(firstname,username,user_id):
    con = pymysql.Connect(host ="localhost",user = "USERNAME",passwd="",database="NAMEDATABASE")
    cs = con.cursor()
    #Search to the database
    com = "SELECT * from support_bot WHERE user_id = %s"
    vel = (user_id)
    cs.execute(com,vel)
    r = cs.fetchall()
    print('select kardam')
#Add user to the database
    if r ==():
        com = "INSERT INTO support_bot (firstname,username,user_id) VALUES (%s,%s,%s)"
        val = (firstname,username,user_id)
        try:
            cs.execute(com,val)
            con.commit()  
        except:
            print('error!')
            con.rollback()
    
        con.close()

def Return_bot(user_id):
    con = pymysql.Connect(host ="localhost",user = "USERNAME",passwd="",database="NAMEDATABASE")
    cs = con.cursor()
    #Search to the database
    com = "SELECT * from support_bot WHERE user_id = %s"
    vel = (user_id)
    cs.execute(com,vel)
    r = cs.fetchall()
#remove user to the database
    if r !=():
        com = "delete from Support_bot where user_id = %s"
        val = (user_id)
        try:
            cs.execute(com,val)
            con.commit()
        except:
            con.rollback()
    
        con.close()

def search_user(user_id):
    con = pymysql.Connect(host ="localhost",user = "USERNAME",passwd="",database="NAMEDATABASE")
    cs = con.cursor()
    #Search to the database
    com = "SELECT * from support_bot WHERE user_id = %s"
    vel = (user_id)
    cs.execute(com,vel)
    r = cs.fetchall()
    if r !=():
        return True
    elif r ==():
        return False


def add_daily_user(firstname,username,chat_id):
    con = pymysql.Connect(host ="localhost",user = "USERNAME",passwd="",database="NAMEDATABASE")
    cs = con.cursor()
    #Search to the database
    com = "SELECT * from daily WHERE chat_id = %s"
    vel = (chat_id)
    cs.execute(com,vel)
    r = cs.fetchall()
    if r ==():
        com = "INSERT INTO daily (firstname,username,chat_id) VALUES (%s,%s,%s)"
        val = (firstname,username,chat_id)
        try:
            cs.execute(com,val)
            con.commit()  
        except:
            print('error!')
            con.rollback()   
        con.close()

def delete_daily_user(firstname,username,chat_id):
    con = pymysql.Connect(host ="localhost",user = "USERNAME",passwd="",database="NAMEDATABASE")
    cs = con.cursor()
    #Search to the database
    com = "SELECT * from daily WHERE chat_id = %s"
    vel = (chat_id)
    cs.execute(com,vel)
    r = cs.fetchall()
    if r !=():
        com = "delete from daily where chat_id = %s"
        val = (chat_id)
        try:
            cs.execute(com,val)
            con.commit()
        except:
            con.rollback()
    
        con.close()

def search_daily():
    con = pymysql.Connect(host ="localhost",user = "USERNAME",passwd="",database="NAMEDATABASE")
    cs = con.cursor()
    #Search to the database
    com = "SELECT * from daily WHERE chat_id"
    cs.execute(com)
    r = cs.fetchall()
    return r


