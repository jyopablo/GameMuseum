from flask import  Flask 
from flask import render_template,flash
from flask import request,redirect,url_for
from werkzeug import secure_filename
import os
import csv

id1=[0]
names=['Usuario']
surnames=['Maestro']
users=['admin']
paswords=['admin']
keys=[0]


id2=[]
name_game=[]
anio_game=[]
precio_game=[] 
categoria_game=[]
foto_game=[]
banner_game=[]
descripcion_game=[]

app = Flask(__name__)
app.config['UPLOAD_FOLDER']="./static/archivos"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#_______________________________________________Pagina principal o index___________________________________________________
@app.route('/')
def index():
	return render_template('index.html')

#_________________________________________________________Login ___________________________________________________________
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
       	 global token
         if user_login=="admin" and pasword_login=="admin":
          token=posicion
          flash('Bienvenido    '+user_login)
          return redirect(url_for('admin')) 
         elif keys[posicion]==0:
          token=posicion
          flash('Bienvenido    '+user_login)
          return redirect(url_for('admin')) 
         else:
          token=posicion 	
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

#___________________________________________Registrar un usuario por su cuenta___________________________________________________
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
              keys.append(1)
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

#_______________________________________________recuperar contraseña ___________________________________________________
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
#_______________________________________________Pagina logeada de un administrador___________________________________________________
@app.route('/admin',methods=['GET','POST'])
def admin():
  try:
    if request.method=="POST":
      search=request.form.get("search")
      verificar1=name_game.count(search)
      global id_ver,name_ver,anio_ver,precio_ver,category_ver,foto_ver,banner_ver,description_ver
      if verificar1 != 0:
        posicion1=name_game.index(search)
        id_ver=id1[posicion1]
        name_ver=name_game[posicion1]
        anio_ver=anio_game[posicion1]
        precio_ver=precio_game[posicion1]
        category_ver=categoria_game[posicion1]
        foto_ver=foto_game[posicion1]
        banner_ver=banner_game[posicion1]
        description_ver=descripcion_game[posicion1]
        return redirect('ver_game')
      else: 
        flash('The video game does not exist')
        return render_template('admin.html')  
    else:          
      return render_template('admin.html')  
  except:
    return render_template('admin.html')  
    
#_______________________________________________Pagina logeada de un usuario___________________________________________________
@app.route('/index2',methods=['GET','POST'])
def index2():
   return render_template('index2.html')    

#_____________________________________________________Perfil de un usuario_________-________________________________________
@app.route('/perfil_index2',methods=['GET','POST'])
def perfil_index2():
  try:
    if request.method=="POST":
      name=request.form.get("name")
      surname=request.form.get("surname")
      user=request.form.get("user")
      pasword=request.form.get("password")
      confirmpassword=request.form.get("confirmpassword")
      if confirmpassword==pasword:
              flash('Update data') 
              names[token]=name
              surnames[token]=surname
              users[token]=user
              paswords[token]=pasword
              return redirect('index2')          
      else:
           user_perfil_index2=users[token]
           surname_perfil_index2=surnames[token]
           name_perfil_index2=names[token]
           pasword_perfil_inedex2=paswords[token]
           flash('Incorrect pasword confirmation')
           return render_template('perfil_index2.html',user_index2=user_perfil_index2,surname_index2=surname_perfil_index2,
           name_index2=name_perfil_index2,pasword_index2=pasword_perfil_inedex2)
    else:
      user_perfil_index2=users[token]
      surname_perfil_index2=surnames[token]
      name_perfil_index2=names[token]
      pasword_perfil_inedex2=paswords[token]
      return render_template('perfil_index2.html',user_index2=user_perfil_index2,surname_index2=surname_perfil_index2,
      name_index2=name_perfil_index2,pasword_index2=pasword_perfil_inedex2)  
  except:
      return flash('User or Confirm of Password, Incorrect')
      user_perfil_index2=users[token]
      surname_perfil_index2=surnames[token]
      name_perfil_index2=names[token]
      pasword_perfil_inedex2=paswords[token]
      return render_template('perfil_index2.html',user_index2=user_perfil_index2,surname_index2=surname_perfil_index2,
      name_index2=name_perfil_index2,pasword_index2=pasword_perfil_inedex2) 

#_______________________________________________Perfil de una de un administrador_______________________________________
@app.route('/perfil_admin',methods=['GET','POST'])
def perfil_admin():
  try:
    if request.method=="POST":
      name=request.form.get("name")
      surname=request.form.get("surname")
      user=request.form.get("user")
      pasword=request.form.get("password")
      confirmpassword=request.form.get("confirmpassword")
      if confirmpassword==pasword:
              flash('Update data') 
              names[token]=name
              surnames[token]=surname
              users[token]=user
              paswords[token]=pasword
              return redirect('admin')          
      else:
           user_perfil_admin=users[token]
           surname_perfil_admin=surnames[token]
           name_perfil_admin=names[token]
           pasword_perfil_admin=paswords[token]
           flash('Incorrect pasword confirmation') 
           return render_template('perfil_admin.html',user_admin=user_perfil_admin,surname_admin=surname_perfil_admin,
           name_admin=name_perfil_admin,pasword_admin=pasword_perfil_admin)
    else:
      user_perfil_admin=users[token]
      surname_perfil_admin=surnames[token]
      name_perfil_admin=names[token]
      pasword_perfil_admin=paswords[token]
      return render_template('perfil_admin.html',user_admin=user_perfil_admin,surname_admin=surname_perfil_admin,
      name_admin=name_perfil_admin,pasword_admin=pasword_perfil_admin) 	  
  except:
      return flash('User or Confirm of Password, Incorrect')
      user_perfil_admin=users[token]
      surname_perfil_admin=surnames[token]
      name_perfil_admin=names[token]
      pasword_perfil_admin=paswords[token]
      return render_template('perfil_admin.html',user_admin=user_perfil_admin,surname_admin=surname_perfil_admin,
      name_admin=name_perfil_admin,pasword_admin=pasword_perfil_admin)          

#_______________________________________________CRUD DE VIDEO JUEGO___________________________________________________
@app.route('/crud',methods=['GET','POST'])
def crud():
   try:
    if request.method=="POST":
      search=request.form.get("search")
      verificar1=name_game.count(search)
      global id_ver,name_ver,anio_ver,precio_ver,category_ver,foto_ver,banner_ver,description_ver
      if verificar1 != 0:
        posicion1=name_game.index(search)
        id_ver=id1[posicion1]
        name_ver=name_game[posicion1]
        anio_ver=anio_game[posicion1]
        precio_ver=precio_game[posicion1]
        category_ver=categoria_game[posicion1]
        foto_ver=foto_game[posicion1]
        banner_ver=banner_game[posicion1]
        description_ver=descripcion_game[posicion1]
        return redirect('ver_game')
      else: 
        flash('The video game does not exist')
        return render_template('crud.html')  
    else:          
       return render_template('crud.html')  
   except:
      return render_template('crud.html') 
      

#_______________________________________________crear un video juego___________________________________________________
@app.route("/crear_game", methods=["GET", "POST"])
def crear_game():
    try:
        if request.method == "POST":
            name = request.form.get("name")
            year = request.form.get("year")
            price = request.form.get("price")
            category = request.form.get("category")
            url = request.form.get("url")
            banner = request.form.get("banner")
            description = request.form.get("description")
            if  name != None and year != None and price != None and url != None and description != None:
                name_game.append(name)
                anio_game.append(year)
                precio_game.append(price)
                categoria_game.append(category)
                foto_game.append(url)
                banner_game.append(banner)
                descripcion_game.append(description)
                if id2:
                   verificar=True
                else:	
                   verificar=False

                if verificar==True:   
                   ultimo=id2[-1]
                   id2.append(ultimo+1)
                else:
                   id2.append(0)
                flash('The video game has been created')
                return redirect(url_for('crud'))
            else:
                flash('Fill in all the fields')
                return render_template("crear_game.html")
        else:    
             return render_template("crear_game.html")      
    except:
        return render_template("crear_game.html")
#_____________________________________________________Ver video juego___________________________________________________
@app.route('/ver_game')
def ver_game():
      return render_template('ver_game.html',id_game=id_ver,name=name_ver,anio=anio_ver,precio=precio_ver,category=category_ver,foto=foto_ver,
	  banner=banner_ver,description=description_ver)     
#_______________________________________________Carga masiva de video juegos____________________________________________
@app.route('/carga_masiva')
def carga_masiva():
      return render_template('carga_masiva.html')    


@app.route("/upload", methods=["GET", "POST"])
def uploader():
    if request.method == "POST":
        f = request.files["archive"]
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        with open('./static/archivos/'+filename) as csvfile:
           reader =csv.reader(csvfile)
           for row in reader:
               if id2:
                   verificar=True
               else: 
                   verificar=False

               if verificar==True:   
                   ultimo=id2[-1]
                   id2.append(ultimo+1)
               else:
                   id2.append(0)
               name_game.append(row[0])
               anio_game.append(row[1])
               precio_game.append(row[2])
               categoria_game.append(row[3]+", "+row[4]+","+row[5])
               foto_game.append(row[6])
               banner_game.append(row[7])
               descripcion_game.append(row[8])
        flash('Successful file')       
        return redirect("admin")
#_______________________________________________Buscar video juego_______________________________________________________
@app.route('/buscar_game', methods=['GET','POST'])
def buscar_game():
	try:
		if request.method=="POST":
			search=request.form.get("search2")
			verificar1=name_game.count(search)
			global id_ver,name_ver,anio_ver,precio_ver,category_ver,foto_ver,banner_ver,description_ver
			if verificar1 != 0:
				posicion1=name_game.index(search)
				id_ver=id1[posicion1]
				name_ver=name_game[posicion1]
				anio_ver=anio_game[posicion1]
				precio_ver=precio_game[posicion1]
				category_ver=categoria_game[posicion1]
				foto_ver=foto_game[posicion1]
				banner_ver=banner_game[posicion1]
				description_ver=descripcion_game[posicion1]
				return redirect('ver_game')
			else:	
				flash('The video game does not exist')
				return render_template('buscar_game.html') 
		else:          
			return render_template('buscar_game.html') 
	except:
		return render_template('buscar_game.html')	
#_______________________________________________Buscar video juego para modificar_______________________________________________________
@app.route('/buscar_game_tres', methods=['GET','POST'])
def buscar_game_tres():
  try:
    if request.method=="POST":
      search=request.form.get("search")
      verificar1=name_game.count(search)
      global id_ver,name_ver,anio_ver,precio_ver,category_ver,foto_ver,banner_ver,description_ver
      if verificar1 != 0:
        posicion_mod=name_game.index(search)
        id_ver=id1[posicion_mod]
        name_ver=name_game[posicion_mod]
        anio_ver=anio_game[posicion_mod]
        precio_ver=precio_game[posicion_mod]
        category_ver=categoria_game[posicion_mod]
        foto_ver=foto_game[posicion_mod]
        banner_ver=banner_game[posicion_mod]
        description_ver=descripcion_game[posicion_mod]
        return redirect('modificar_game')
      else: 
        flash('The video game does not exist')
        return render_template('buscar_game_tres.html') 
    else:          
      return render_template('buscar_game_tres.html') 
  except:
    return render_template('buscar_game_tres.html')
#_______________________________________________Modificar video juego_______________________________________________________
@app.route("/modificar_game", methods=["GET", "POST"])
def modificar_game():
    try:
        if request.method == "POST":
            name = request.form.get("name")
            year = request.form.get("year")
            price = request.form.get("price")
            category = request.form.get("category")
            url = request.form.get("url")
            banner = request.form.get("banner")
            description = request.form.get("description")
            if  name != None and year != None and price != None and url != None and description != None:
                name_game[id_ver]=name
                anio_game[id_ver]=year
                precio_game[id_ver]=price
                categoria_game[id_ver]=category
                foto_game[id_ver]=url
                banner_game[id_ver]=banner
                descripcion_game[id_ver]=description
                flash('The video game has been modify')
                return redirect('crud')
            else:
                flash('Fill in all the fields')
                return render_template('modificar_game.html',name=name_ver,anio=anio_ver,precio=precio_ver,category=category_ver,foto=foto_ver,
                banner=banner_ver,description=description_ver) 
        else:
             return render_template('modificar_game.html',name=name_ver,anio=anio_ver,precio=precio_ver,category=category_ver,foto=foto_ver,
             banner=banner_ver,description=description_ver)    
    except:
         return render_template('modificar_game.html',name=name_ver,anio=anio_ver,precio=precio_ver,category=category_ver,foto=foto_ver,
         banner=banner_ver,description=description_ver) 


#_______________________________________________Eliminar video  Game_______________________________________________________
@app.route('/buscar_game_dos', methods=['GET','POST'])
def buscar_game_dos():
	try:
		if request.method=="POST":
			search=request.form.get("search")
			verificar=name_game.count(search)
			if verificar != 0:
				posicion1=name_game.index(search)
				id1.pop(posicion1)
				name_game.pop(posicion1)
				anio_game.pop(posicion1)
				precio_game.pop(posicion1)
				categoria_game.pop(posicion1)
				foto_game.pop(posicion1)
				banner_game.pop(posicion1)
				descripcion_game.pop(posicion1)
				flash('The video game removed')
				return redirect('crud')
			else:	
				flash('The video game does not exist')
				return render_template('buscar_game_dos.html') 
		else:          
			return render_template('buscar_game_dos.html') 
	except:
		return render_template('buscar_game_dos.html')

#_______________________________________________Crear usuario adminitrador_______________________________________________________
@app.route('/crear_usuario', methods=['GET','POST'])
def crear_usuario():
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
              keys.append(0)
              ultimo=id1[-1]
              id1.append(ultimo+1)
              return redirect('admin')          
           else:
              return flash('User or Confirm of Password, Incorrect') 
              return render_template('crear_usuario.html')
      else:
        return render_template('crear_usuario.html')
    else: 
      return render_template('crear_usuario.html')    
  except:
      return flash('User or Confirm of Password, Incorrect')  
      return render_template('crear_usuario.html')
  
#_______________________________________________Catalogo de videojuegos_______________________________________________________  



if __name__=='__main__':
    app.run(threaded=True,debug=True,port=8000)	