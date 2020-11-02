from flask import Flask,render_template,request

import sqlite3 as sql

#Init app
app = Flask(__name__)



#API to fetch all match details sorted according to dates
@app.route('/matchlist')
def matchlist():
    try:
       with sql.connect("database.db") as conn:    
            conn.row_factory = sql.Row 
            cur = conn.cursor()
            cur.execute("SELECT team_a, team_b, winner, match_date from matches ORDER BY match_date")
            rows = cur.fetchall()
            msg="Printed successfully"
    except:
        conn.rollback()
        msg="error in print operation"
    finally:
        return render_template("matchlist.html",rows=rows)
        conn.close()

#APT to add match details in SQL database
@app.route('/addrec',methods = ['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            name1 = request.form['namea']
            name2 = request.form['nameb']
            score1 = request.form['scorea']
            wicket1 = request.form['wicketa']
            four1 = request.form['foura']
            six1 = request.form['sixa']
            score2 = request.form['scoreb']
            wicket2 = request.form['wicketb']
            four2 = request.form['fourb']
            six2 = request.form['sixb']
            winner = request.form['winner']
            man = request.form['manofmatch']
            date = request.form['dateofmatch']

            with sql.connect("database.db") as conn:
                cur = conn.cursor()

                cur.execute("INSERT INTO matches(team_a, score_a, wicket_a, four_a, six_a, team_b, score_b, wicket_b, four_b,six_b, winner, man_of_match,match_date) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(name1,score1,wicket1,four1,six1,name2,score2,wicket2,four2,six2,winner,man,date))
                conn.commit()
                msg = "Record successfully added"

        except:
            conn.rollback()
            msg="error in insert operation"

        finally:
            return render_template('result.html',msg=msg)
            conn.close()

#API to add team details in the SQL database
@app.route('/addrec2',methods=['POST','GET'])
def addrec2():
    if request.method == 'POST':
        try:
            name = request.form['name']
            name1 = request.form['coname']
            name2 = request.form['caname']
            number = request.form['num']
    
            with sql.connect("database.db") as conn:
                cur = conn.cursor()
                
                #Insert a row of data
                cur.execute("INSERT INTO teams(team_name, coach_name, captian_name, no_match) VALUES(?,?,?,?)",(name,name1,name2,number))
                
                #Save (commit) the changes
                conn.commit()
                msg = "Record successfully added"

        except:
            conn.rollback()
            msg="error in insert operation"

        finally:
            return render_template('result.html',msg=msg)
            #Close the connection
            conn.close()

#API to fetch details of a specific match from SQL database
@app.route('/addrec1',methods = ['POST','GET'])
def addrec1():
    if request.method == 'POST':
        rows=[]
        rows1=[]
        rows2=[]
        name1={}
        name2={}
        try:
            name1 = request.form['namea']
            name2 = request.form['nameb']

            with sql.connect("database.db") as conn:
                conn.row_factory=sql.Row
                cur = conn.cursor()
                
                cur.execute("SELECT team_a,score_a,wicket_a,four_a, six_a, team_b, score_b, wicket_b, four_b, six_b, winner,man_of_match FROM matches WHERE team_a=? AND team_b=? ",(name1,name2))
                rows = cur.fetchall()

            with sql.connect("database.db") as conn1:    
                conn1.row_factory=sql.Row
                cur = conn1.cursor()
                cur.execute("SELECT * from teams WHERE team_name=?",(name1))
                rows1=cur.fetchall()

            with sql.connect("database.db") as conn2:    
                conn2.row_factory=sql.Row
                cur = conn2.cursor()
                cur.execute("SELECT * from teams WHERE team_name=?",(name2))
                rows2=cur.fetchall()

                msg = "Record displayed successfully"

        except:
            conn.rollback()
            msg="error in display operation"

        finally:
            return render_template("result1.html",**locals())
            #Close the connection
            conn.close()

#API to direct to home page
@app.route('/')
def home():
    return render_template('home.html')

#API to direct to take input of match details 
@app.route('/match')
def new_match():
    return render_template('match.html')

#API to direct to get details of a specific match
@app.route('/matchdetails')
def matchdetails():
    return render_template('matchdetails.html')

#API to direct to add teams page
@app.route('/team')
def new_team():
    return render_template('team.html')  
            
#RUn server
if __name__ == '__main__':
  app.run(debug=True)