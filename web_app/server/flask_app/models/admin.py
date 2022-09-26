from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Admin:
    def __init__(self, data):
        self.id=data["id"]
        self.name=data["name"]
        self.lastname=data["lastname"]
        self.email=data["email"]
        self.password=data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, formulario):
        #formulario = {
        #     "name": "Jhomar",
        #     "lastname": "Astuyauri",
        #     "email": "jhomarcristianelias@gmail.com",
        #     "password": "HackathonIntercon!!!2022"
        # }
        query = "INSERT INTO admins (name, lastname, email, password) VALUES (%(name)s, %(lastname)s, %(email)s, %(password)s)"
        nuevoId = connectToMySQL('tollkit_esquema').query_db(query, formulario)
        return nuevoId

    @staticmethod
    def valida_usuario(formulario):
        #formulario = {
        #     "name": "Jhomar",
        #     "lastname": "Astuyauri",
        #     "email": "jhomarcristianelias@gmail.com",
        #     "password": "HackathonIntercon!!!2022"
        # }
        es_valido = True
        #Validar que mi nombre sea mayor a 2 caracteres
        if len(formulario['name']) < 2:
            flash('Tu nombre debe de tener al menos 2 caracteres', 'registro')
            es_valido = False
        #Validar que mi apellido sea mayor a 2 caracteres
        if len(formulario['lastname']) < 2:
            flash('Tu apellido debe de tener al menos 2 caracteres', 'registro')
            es_valido = False
        #Valido email con expresiones regulares abc123@21msn.com ->NO te aceptaría a.com
        if not EMAIL_REGEX.match(formulario['email']):
            flash('E-mail inválido', 'registro')
            es_valido = False
        if len(formulario['password']) < 8:
            flash('La contraseña debe tener al menos 8 caracteres', 'registro')
            es_valido = False
        if formulario['password'] != formulario['password_confirm']:
            flash('Las contraseñas no coinciden', 'registro')
            es_valido = False
        #Consulta si ya existe ese correo
        query = "SELECT id FROM admins WHERE email = %(email)s"
        results = connectToMySQL('tollkit_esquema').query_db(query, formulario)
        #results = [
        #     {"name": "Jhomar", "lastname":"Astuyauri"}
        # ]
        if len(results) >= 1:
            flash('E-mail registrado previamente', 'registro')
            es_valido = False

        return es_valido

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM admins WHERE id = %(id)s"
        result = connectToMySQL('tollkit_esquema').query_db(query, data)
        if len(result) < 1:
            return False
        else :
            usr = result[0]
            user = cls(usr)
            return user

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM admins WHERE email = %(email)s"
        result = connectToMySQL('tollkit_esquema').query_db(query, data)
        if len(result) < 1:
            return False
        else :
            usr = result[0]
            user = cls(usr)
            return 