from flask import  Flask 
from flask import render_template,flash
from flask import request,redirect,url_for
from werkzeug import secure_filename
import os

id1=[0]
names=['Usuario']
surnames=['Maestro']
users=['admin']
paswords=['admin']

id2=[]
name=[]
Anio=[]
Precio=[] 
Categoria=[]
Foto=[]
Banner=[]
Descripcion=[]

app = Flask(__name__)
app.config['UPLOAD_FOLDER']="./static/archivos"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


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
          flash('Bienvenido    '+user_login) 
          return redirect(url_for('admin')) 
         else:
          flash('Bienvenido    '+user_login) 
          return redirect('index2')
       else:
         flash('Incorrect User or Password') 
         return render_template('login.html')  
    else: 
      return render_template('login.html') 
  except:
       flash('Incorrect User or Password')
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
              flash('User Registered ') 
              names.append(name)
              surnames.append(surname)
              users.append(user)
              paswords.append(pasword)
              ultimo=id1[-1]
              id1.append(ultimo+1)
              return redirect('login')          
           else:
              return render_template('registrar.html')
      else:
        return render_template('registrar.html')
    else:
      return render_template('registrar.html')    
  except:
      return flash('User or Confirm of Password, Incorrect')  
      return render_template('registrar.html') 


@app.route('/recuperar', methods=['GET','POST'])
def recuperar():
  try:
   if request.method=="POST":
     user_recover=request.form.get("username")
     position_recover=users.index(user_recover)
     if position_recover != 0 and user_recover != None:
        pasword_recover=paswords[position_recover]
        flash('Su contraseña es: '+pasword_recover) 
        return render_template('recuperar.html')
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

@app.route('/perfil_index2')
def perfil_index2():
   return render_template('perfil_index2.html')


@app.route('/carga_masiva')
def carga_masiva():
      return render_template('carga_masiva.html')    

@app.route('/upload', methods=['GET','POST'])
def uploader():
  if request.method=="POST":
      f=request.files['archive']
      filename=secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
      return "Archivo subido exitosamente"  

if __name__=='__main__':
    app.run(threaded=True,debug=True,port=8000)	