from flask import  Flask 
from flask import render_template
from flask import request,redirect,url_for
from werkzeug import secure_filename
import os

id=[0]
names=['Usuario']
surnames=['Maestro']
users=['admin']
paswords=['admin']

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
  try:
    if request.method=="POST":
       user_login=request.form.get("username")
       pasword_login=request.form.get("password")
       posicion=users.index(user_login)
       U_login=user_login==users[posicion]
       P_login=pasword_login==paswords[posicion]
       if U_login==True and P_login==True and user_login != None and pasword_login != None:
        if user_login=="admin" and pasword_login=="admin": 
          return redirect('admin') 
        else:
          return redirect('index2')
       else:
         return render_template('login.html')  
    else: 
      return render_template('login.html') 
  except:
       return render_template('login.html')

@app.route('/registrar',methods=['GET','POST'])
def registrar():
  try:
    if request.method=="POST":
      name=request.form.get("name")
      surname=request.form.get("surname")
      user=request.form.get("user")
      pasword=request.form.get("password")
      confirmpassword=request.form.get("confirmpassword")
      verificar=users.count(user)
      if verificar==0 and name != None and surname != None and user != None and pasword != None and confirmpassword != None :
           if confirmpassword==pasword:
              names.append(name)
              surnames.append(surname)
              users.append(user)
              paswords.append(pasword)
              ultimo=id[-1]
              id.append(ultimo+1)
              return redirect('login')          
           else:
              return render_template('registrar.html')
      else:
        return render_template('registrar.html')
    else:
      return render_template('registrar.html')    
  except:
      return render_template('registrar.html') 


@app.route('/recuperar', methods=['GET','POST'])
def recuperar():
  try:
   if request.method=="POST":
     user_recover=request.form.get("username")
     position_recover=users.index(user_recover)
     if position_recover != 0 and user_recover != None:
        pasword_recover=paswords[position_recover]
        return(pasword_recover)
     else:
        return render_template('recuperar.html')
   else:
      return render_template('recuperar.html')
  except:
      return render_template('recuperar.html')

@app.route('/admin')
def admin():
    return render_template('admin.html') 

@app.route('/index2')
def index2():
   return render_template('index2.html')    


@app.route('/carga_masiva')
def carga_masiva():
      return render_template('carga_masiva.html')    


if __name__=='__main__':
    app.run(threaded=True,debug=True,port=8000)	