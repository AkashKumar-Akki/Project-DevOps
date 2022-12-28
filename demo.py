import sqlite3
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def demo():
        return render_template('Login.html')
conn = sqlite3.connect('AkashDB.db')
print("Opened database successfully");

# conn.execute('CREATE TABLE Users (txt TEXT, email TEXT, pswd TEXT)')
# print("Table created successfully");
# conn.close()




# @app.route('/signup' , methods=['POST','GET'])
# def signup():
#         user=request.form['txt']
#         email=request.form['email']
#         pwd=request.form['pswd']
#         return render_template('pass.html',a=user,b=email,c=pwd)
        
        
@app.route("/sign-up",methods = ["POST","GET"])  
def signup():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["txt"]  
            email = request.form["email"]  
            password = request.form["pswd"]  
            with sqlite3.connect("AkashDB.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Users (txt, email, pswd) values (?,?,?)",(name,email,password))  
                con.commit()  
                msg = "User successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the User to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()        

if __name__ == '__main__':
        app.run(debug=True);
        