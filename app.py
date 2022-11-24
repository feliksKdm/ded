from flask import Flask, render_template, redirect, url_for, request, url_for
import sqlite3
import pandas as pd

app = Flask(__name__)

con = sqlite3.connect("data.db", check_same_thread=False)
cur = con.cursor()

@app.route("/")
def index():
    

    # conn = sqlite3.connect('data.db', isolation_level=None,
    #                     detect_types=sqlite3.PARSE_COLNAMES)
    # db_df = pd.read_sql_query("SELECT * FROM Coladatas", conn)
    # db_df.to_csv('database.csv', index=False)
    return render_template("main-wnd1.html")

@app.route("/signup")
def CCsurvey():
    return render_template('signup.html')

@app.route('/signed', methods = ['POST'])
def signed():
    email = request.form.get('email')
    password = request.form.get('password')

    cur.execute(' create table if not exists users([id] INTEGER PRIMARY KEY,[email] text, [password] text)')
    cur.execute('INSERT INTO users(email, password) values (?, ?)' , (email , password))
    return render_template('CCsurvey.html')

@app.route("/CocaColasurvey")
def CocaColasurvey():
    return render_template('CCsurvey.html')

@app.route("/Colaform", methods = ['POST'])
def Colaform():
    Age = request.form.get('Age')
    sex = request.form.get('sex')
    
    promo = request.form.get('promoAcc')
    promo_size = request.form.get('promoAcc-size')

    prefer_Cola = request.form.get('3-Coca-Cola')
    prefer_Cola_Zero = request.form.get('3-Coca-Cola Zero')
    prefer_Fanta = request.form.get('3-Fanta')
    prefer_Sprite = request.form.get('3-Sprite')
    prefer_Schwepppes = request.form.get('3-Schweppes')
    prefer_Bonaqua = request.form.get('3-Bonaqua')
    prefer_Fuse = request.form.get('3-Fuse tea')

    liter_zero_twofive = request.form.get('zero-twofive')
    liter_zero_five = request.form.get('zero-five')
    liter_one = request.form.get('one')
    liter_one_five = request.form.get('one-five')
    liter_two = request.form.get('two')



    cur.execute(
        "CREATE TABLE IF NOT EXISTS Coladatas([id] INTEGER PRIMARY KEY,[Age] INT, [sex] STRING , [played_inpromo] INT, [promo_size],                      [prefer_CocaCola] INT, [prefer_CocaCola_Zero] INT, [prefer_Fanta] INT, [prefer_Sprite] INT, [prefer_Schweppes] INT, [prefer_Bonaqua] INT, [prefer_Fuse] INT,                 [liter_zero_twofive] INT, [liter_zero_five] INT, [liter_one] INT, [liter_one_five] INT, [liter_two] INT)")
    cur.execute(
        "INSERT INTO Coladatas (Age, sex,played_inpromo, promo_size ,prefer_CocaCola, prefer_CocaCola_Zero, prefer_Fanta, prefer_Sprite, prefer_Schweppes, prefer_Bonaqua, prefer_Fuse,   liter_zero_twofive,  liter_zero_five, liter_one, liter_one_five, liter_two) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (Age, sex, promo, promo_size, prefer_Cola, prefer_Cola_Zero, prefer_Fanta,prefer_Sprite, prefer_Schwepppes, prefer_Bonaqua, prefer_Fuse, liter_zero_twofive, liter_zero_five, liter_one,liter_one_five,liter_two)
    )
    con.commit()
    return redirect('/sendedColaform')

@app.route('/sendedColaform')
def submitedColaform():
    
    all_Coladatas = cur.execute("SELECT * FROM Coladatas").fetchall()
    return render_template("survey_succes.html", datas=all_Coladatas)
