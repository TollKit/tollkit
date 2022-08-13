from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import tollkit

class Student:
    def __init__(self, data):
        self.id=data["id"]
        self.name=data["name"]
        self.lastname=data["lastname"]
        self.temp=data["temp"]
        self.has_mask=data["has_mask"]
        self.has_studentCard=data["has_studentCard"]
        self.has_alcohol=data["has_alcohol"]
        self.has_covidCard=data["has_covidCard"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        # Creamos una lista para mostrar qué Tollkits están relacionados con el estudiante.
        self.by_tollkit = []

    @classmethod #CORREGIR
    def save( cls , data ):
        query = "INSERT INTO toppings ( topping_name, created_at , updated_at ) VALUES (%(topping_name)s,NOW(),NOW());"
        return connectToMySQL('burgers').query_db(query, data)

    # Este método recuperará el estudiante específico junto con todos los Tollkits asociados a él.
    @classmethod
    def get_student_with_tollkit(cls, data):
        query= """
            SELECT * FROM students LEFT JOIN students_has_tollkits ON students_has_tollkits.students_id = students_id LEFT JOIN tollkits ON students_has_tollkits.tollkits_id = tollkits.id WHERE students.id = %(id)s;
        """
        results =  connectToMySQL('esquema_tollkit_intercon').query_db( query , data )
        # los resultados serán una lista de objetos student con el tollkit adjunto a cada fila 
        student = cls( results[0] )
        for i in results:
            # ahora parseamos los datos student para crear instancias de estudiante y agregarlas a nuestra lista
            tollkit_data = {
                "id" : i["tollkits.id"],
                "number_door" : i["number_door"],
                "has_alcohol" : i["has_alcohol"],
                "created_at" : i["students.created_at"],
                "updated_at" : i["students.updated_at"]
            }
            # Agregamos un tollkit a la lista de un estudiante específico
            student.by_tollkit.append( tollkit.Tollkit( tollkit_data ) )
        return student


