import mysql.connector
from datetime import date
from pymongo import MongoClient

connection = "mongodb+srv://dvnber2001:BvtpT7WKpomWZaTG@cluster0.elmoehx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(connection)

database_mongo= client["Api"]
collection_mongo = database_mongo["Usuarios"]
#creacion de un registro en mongo db
def create_register_mongo(nombre,edad,talento):
    documento = {'nombre': nombre, 'edad': edad , 'talento':talento}
    result = collection_mongo.insert_one(documento)
    print('ID del documento insertado:', result.inserted_id)

#leer registros en mongo
def read_mongo(nombre):
    document = collection_mongo.find_one({"nombre":nombre})
    print('Documento encontrado:', document)

#actualizar un registro en mongo

def update_register_mongo(nombre,edad,talento):
    filtro = {'nombre': nombre}
    nuevos_valores = {'$set': {'edad': edad, 'talento': talento}}
    resultado = collection_mongo.update_one(filtro, nuevos_valores)
    print('Documentos actualizados:', resultado.modified_count)

#eliminar registro en mongo
def delete_mongo(nombre):
    filter={'nombre': nombre}
    result = collection_mongo.delete_one(filter)
    print('Documentos eliminados:', result.deleted_count)

          
#creación de la connexion (variables de conexión) 
def connection():
    return mysql.connector.connect(
        host = "127.0.0.1",
        port = "3306",
        user = "root",
        password = "Ilovereggae.17",
        database = "employees"
    )

#creacion de un registro en la base de datos y la tabla employees

def create_register(id, birth_date, firts_name, last_name, gender, hire_date):
    #creacion de la consulta a hacer 
    query= "INSERT INTO employees (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES (%s,%s,%s,%s,%s,%s)"
    #insercion de los valores en la query
    values=(id, birth_date, firts_name, last_name, gender, hire_date)
    #llamada de la conexion 
    con = connection()
    cursor = con.cursor()
    #ejecucion de la conexion 
    cursor.execute(query,values)
    #devolucion del resultado
    print (f"Usuario {firts_name} insertado con éxito.")

#lectura de los datos en la tabla employees
def read_registers():

    #repeticion de los pasos para hacer  las consultas
    query = "SELECT * FROM employees"
    con = connection()
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)

#actualizacion de un usuario en la base de datos
def update_register(id,birth_date, firts_name, last_name, gender, hire_date):

    #repeticion de los pasos para hacer las consultas
    query= "UPDATE employees SET birth_date = %s, first_name =%s, last_name=%s, gender=%s, hire_date=%s WHERE emp_no = %s"
    values=(birth_date, firts_name, last_name, gender, hire_date, id)
    con = connection()
    cursor = con.cursor()
    cursor.execute(query,values)
    connection.commit()
    print(f"Usuario con ID {id} actualizado con éxito.")

#borrado de un usuario en la base de datos
def delete_register(id):

    #repeticion de los pasos para hacer las consultas
    query = "DELETE FROM employees WHERE emp_no = %s"    
    values= (id,)
    con = connection()
    cursor = con.cursor()
    cursor.execute(query,values)
    print(f"Usuario con ID {id} eliminado con éxito.")

#seccion para insertar datos
def leer_datos_mysql():
    selection = int(input("selecciona una accion \n 1) Crear empleado \n 2) Ver empleados \n 3) actualizar empleados \n 4) Borrar empleado \n 0) Salir \n"))

    while(selection != 0):
        if(selection == 1):
            id = input("ingrese el id \n")
            nombre= input("ingrese el nombre \n")
            apellido= input("ingrese el apellido  \n")
            diaN= int(input("ingresa el dia de nacimiento \n"))
            MesN= int(input("ingresa el mes de nacimiento \n"))
            AnoN= int(input("ingresa el año de nacimiento \n"))
            fecha_nacimineto = date(AnoN, MesN, diaN)
            genero= input("ingrese el Genero F o M \n")
            diaC= int(input("ingresa el dia de contratacion \n"))
            MesC= int(input("ingresa el mes de contratacion \n"))
            AnoC= int(input("ingresa el año de contratacion \n"))
            Fecha_contratacion= date(AnoC,MesC,diaC)

            #llamada al metodo de creación
            create_register(id,fecha_nacimineto, nombre, apellido, genero, Fecha_contratacion)
        elif(selection ==2):
            #llamada al metodo de lectura 
            read_registers()
        elif(selection ==3):
            id = input("ingrese el id \n")
            nombre= input("ingrese el nombre\n")
            apellido= input("ingrese el apellido\n")
            diaN= int(input("ingresa el dia de nacimiento \n"))
            MesN= int(input("ingresa el mes de nacimiento \n"))
            AnoN= int(input("ingresa el año de nacimiento \n"))
            fecha_nacimineto = date(AnoN, MesN, diaN)
            genero= input("ingrese el Genero F o M \n")
            diaC= int(input("ingresa el dia de contratacion \n"))
            MesC= int(input("ingresa el mes de contratacion \n"))
            AnoC= int(input("ingresa el año de contratacion \n"))
            Fecha_contratacion= date(AnoC,MesC,diaC)
            #llamada al metodo de actualización
            update_register(id,fecha_nacimineto, nombre, apellido, genero, Fecha_contratacion)
        elif(selection == 4):
            id = int(input("ingrese el id\n"))
            #llamada al metodo de borrado
            delete_register(id)
        selection = int(input("selecciona una accion \n 1) Crear empleado \n 2) Ver empleados \n 3) actualizar empleados \n 4) Borrar empleado \n 0) Salir \n"))
def leer_datos_mongo():
    selection = int(input("selecciona una accion \n 1) Crear usuario \n 2) Ver usuario \n 3) actualizar usuario \n 4) Borrar usuario \n 0) Salir \n"))
    while(selection != 0):
        if(selection == 1):
            nombre= input("ingrese el nombre del usuario")
            edad = int(input("ingrese edad del usuario"))
            talento = input("ingrese el talento del usuario")
            create_register_mongo(nombre,edad,talento)
        elif(selection == 2):
            nombre= input("ingrese el nombre del usuario")
            read_mongo(nombre)
        elif(selection == 3):
            nombre= input("ingrese el nombre del usuario")
            edad = int(input("ingrese nueva edad  del usuario"))
            talento = input("ingrese el nuevo talento del usuario")
        elif(selection == 4):
            nombre= input("ingrese el nombre del usuario")
            delete_mongo(nombre)
    
        selection = int(input("selecciona una accion \n 1) Crear usuario \n 2) Ver usuario \n 3) actualizar usuario \n 4) Borrar usuario \n 0) Salir \n"))

#llamado de cada base de datos
selection = int(input("selecciona una accion \n 1) usar MySQL \n 2) usar Mongo \n 0) Salir \n"))
if(selection==1):
    leer_datos_mysql()
elif(selection == 2):
    leer_datos_mongo()
#cerrar la conexion a la base de datos al termianr los procesos


con = connection()
con.close()
client.close()