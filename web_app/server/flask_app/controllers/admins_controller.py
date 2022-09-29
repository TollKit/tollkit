from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.admin import Admin
from flask_app.models.tollkit import Tollkit
from flask_app.models.university import University
#from flask_bcrypt import Bcrypt
from flask_app.mqtt import subscriber_rfid,subscriber_temp, subscriber_alcohol
from flask_app.QRcard_vacunation import web_selenium
from flask_app.faceMask_detection import detect_mask_video
#bcrypt = Bcrypt(app)
from subprocess import *
import time
# pip install subprocess.run

@app.route("/")
def index():
    # dicc = subscriber.main()
    # return f"{dicc}"
    return render_template("home.html")

@app.route("/register-view")
def register_view():
    return render_template("register.html")

@app.route("/register")
def register():
    if not Admin.valida_usuario(request.form):
        return redirect("/")
    # Agregamos nuestro nuevo PASSWORD ENCRIPTADO
    pwd=bcrypt.generate_password_hash(request.form["password"])
    # CREAMOS nuestro nuevo diccionario con la PASSSWORD PROTEGIDA
    formulario={
        "name":request.form["name"],
        "lastname":request.form["lastname"],
        "email":request.form["email"],
        "password":pwd,
    }
    id = Admin.save(formulario)

    session["user_id"]=id

    return redirect("/dashboard")

@app.route("/login-view")
def login_view():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    user=Admin.get_by_email(request.form)
    if not user:
        flash("Email no encontrado" , "login")
        return redirect("/")

    if not (bcrypt.check_password_hash(user.password, request.form["password"])):
        flash("Password Incorrecto", "login")
        return redirect("/")

    session["user_id"] = user.id

    return redirect("/dashboard")

@app.route("/dashboard", methods=["POST"])
def dashboard():
    # if "user_id" not in session:
    #     return redirect("/")
    
    # data={
    #     "id":session["user_id"]
    # }

    # Le mando mis datos y recibo un OBJETO USUARIO   
    # Usuario que INICIÓ SESIÓN  
    # user=Admin.get_by_id(data)

    # # Agregamos las products
    # products=Tollkit.get_all()
    lista_dicc = []
    print("==================[INICIALIZANDO TOLLKIT]==================")
    print("----[Paso 1: DETECTANDO SU MASCARILLA]----")
    # print(call(["python", "detect_mask_video.py"]))
    data_mask_status = detect_mask_video.detect_mask_flask()
    print(data_mask_status)
    if data_mask_status==True and data_mask_status!=None:
        print("----[Paso 2: MUESTRE SU CARNET DE VACUNACIÓN]----")
        data_qr_card= web_selenium.main()
        print(data_qr_card)
        if data_qr_card:
            print("----[Paso 3: IDENTIFICANDO SU TEMPERATURA]----")
            data_temp = subscriber_temp.main()

            print("----[Paso 4: DETECTANDO SU CARNET UNIVERSITARIO]----")
            data_rfid = subscriber_rfid.main()
            
            # Paso 5: Alcohol en gel
            print("----[Paso 5: DISPENSANDO ALCOHOL EN GEL]----")
            data_alcohol = subscriber_alcohol.main()

    
    fecha_actual=time.strftime("%Y-%m-%d")
    print(fecha_actual)
    # temp_fecha_actual = time.strptime(fecha_actual, "%Y-%m-%d")

    dicc={
        "temp":data_temp,
        "has_studentCard":data_rfid,
        "has_covidCard":data_qr_card[1],
        "name":data_qr_card[0],
        "has_mask":data_mask_status,
        "has_alcohol":data_alcohol,
        "date": fecha_actual,
    }
    lista_dicc.append(dicc)
    print(lista_dicc)

    return render_template("dashboard.html", lista_dicc=lista_dicc)

@app.route("/tollkit-user")
def tollkit_user():
    
    return render_template("tollkit_user.html")

@app.route("/logout")
def logout():
    # Con este clear() borramos todas nuestras sessiones
    session.clear()
    return redirect("/")
