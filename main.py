"""
==============================================
PyMongo + MongoDB 
==============================================

ANTES DE EJECUTAR:
docker run -d -p 27017:27017 --name mongodb mongo

Crear ambiente virtual igual que en otras actividades
Activar ambiente virtual

Instalar dependencia:
pip install pymongo

"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import json


# -------------------------------------------------
# CONEXIÓN
# -------------------------------------------------

try:
    # TODO: Crear el MongoClient apuntando a mongodb://localhost:27017/
    client = MongoClient('mongodb://127.0.0.1:27017/')

except ConnectionFailure:
    print("Error de conexión")
    exit()

# TODO: Crear / obtener base de datos llamada "mi_base"
db = client['mi_base']

# TODO: Obtener colección llamada "usuarios"
coll = db.create_collection("usuarios")



# -------------------------------------------------
# 1. INSERTAR
# -------------------------------------------------
def insertar():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")
    activo = input("¿Activo? (true/false): ").lower() == "true"
    rol = input("Rol: ")

    # TODO: Insertar documento
    users_document = {
        'nombre': nombre,
        'edad': edad,
        'ciudad': ciudad,
        'activo': activo,
        'rol': rol
    }

    coll.insert_one(users_document)
# end def



# -------------------------------------------------
# 2. INSERTAR VARIOS
# -------------------------------------------------
def insertar_varios():

    print("Pega una lista JSON:")
    datos = input("JSON: ")

    # Esto carga todos los documentos.
    documentos = json.loads(datos)

    # TODO: Insertar con insert_many
    coll.insert_many(documentos)
# end def

# -------------------------------------------------
# 3. MOSTRAR TODOS
# -------------------------------------------------
def mostrar_todos():

    print("\n--- TODOS LOS DOCUMENTOS ---")

    # TODO: Obtener documentos con find()
    users = coll.find()

    # TODO: Recorrer e imprimir
    for u in users:
        print(f'Nombre: {u.get('nombre')}\nEdad: {u.get('edad')}\nCiudad: {u.get('ciudad')}\nActivo: {u.get('activo')}\nRol: {u.get('rol')}')
    # end for-in
# end def

# -------------------------------------------------
# 4. BUSCAR POR EDAD
# -------------------------------------------------
def buscar_con_filtro():

    edad = int(input("Buscar usuarios con edad mayor a: "))

    # TODO: Crear query con $gt
    gt_query = {'edad': {'$gt': edad}}

    # TODO: Ejecutar búsqueda
    gt_find = coll.find(gt_query)

    # TODO: Imprimir resultados
    for u in gt_find:
        print(f'Nombre: {u.get('nombre')}\nEdad: {u.get('edad')}\nCiudad: {u.get('ciudad')}\nActivo: {u.get('activo')}\nRol: {u.get('rol')}')
    # end for-in
# end def

# -------------------------------------------------
# 5. BUSCAR ACTIVOS
# -------------------------------------------------
def buscar_activos():
    # TODO: Crear un query donde activo sea True
    active_query = {'activo': True}

    # TODO: Buscar documentos donde activo sea True
    active = coll.find(active_query)

    # TODO: Imprimir resultados
    for u in active:
        print(f'Nombre: {u.get('nombre')}\nEdad: {u.get('edad')}\nCiudad: {u.get('ciudad')}\nActivo: {u.get('activo')}\nRol: {u.get('rol')}')
    # end for-in
# end def

# -------------------------------------------------
# 6. BUSCAR POR CIUDAD
# -------------------------------------------------
def buscar_por_ciudad():
    # estoy segura que la indicación es otra pero no entiendo si quiere que le pida al user la ciudad porque lo hace abajo, usaré lo que me enseñó un tal Anand en stack overflow

    # TODO: Buscar por ciudad
    city = coll.aggregate([{'$group': {'_id': 'ciudad'}}])

    # TODO: Imprimir resultados
    for u in city:
        print(f'Nombre: {u.get('nombre')}\nEdad: {u.get('edad')}\nCiudad: {u.get('ciudad')}\nActivo: {u.get('activo')}\nRol: {u.get('rol')}')
    # end for-in
# end def


# -------------------------------------------------
# 7. BUSCAR CON PROYECCIÓN
# -------------------------------------------------
def buscar_con_proyeccion():

    ciudad = input("Ciudad: ")

    # TODO: Buscar por ciudad mostrando solo nombre y rol sin _id
    city = coll.find({'ciudad': ciudad}, {'nombre':1, 'rol':1})

    # TODO: imprimir 
    for u in city:
        print(f'Nombre: {u.get('nombre')}\nRol: {u.get('rol')}')


# -------------------------------------------------
# 8. FIND ONE
# -------------------------------------------------
def buscar_uno():
    # TODO: pedir el nombre y edad
    name = input('Nombre: ')
    age = int(input('Edad: '))

    # TODO: Usar find_one
    query = coll.find_one({'$and' : [{'nombre': name}, {'edad': age}] })

    # TODO: imprimir resultados
    for u in query:
        print(f'Nombre: {u.get('nombre')}\nEdad: {u.get('edad')}\nCiudad: {u.get('ciudad')}\nActivo: {u.get('activo')}\nRol: {u.get('rol')}')
    # end for-in
# end def


# -------------------------------------------------
# 9. CONTAR DOCUMENTOS
# -------------------------------------------------
def contar():

    # TODO: Contar todos los documentos


    # TODO: Contar con filtro por ciudad
    pass


# -------------------------------------------------
# 11. ACTUALIZAR ROL
# -------------------------------------------------
def actualizar():
    nombre = input("Nombre a actualizar: ")
    rol = input("Nuevo rol: ")

    # TODO: Buscar por nombre y actualizar el rol
    res = coll.update_one({'nombre': nombre},{'$set': {'rol': rol}})
    print(f'Actualizado: {res.modified_count}')

# -------------------------------------------------
# 12. ACTIVAR USUARIOS INACTIVOS
# -------------------------------------------------
def actualizar_varios():
    # TODO: actualizar donde activo sea False y cambiar a True
    res = coll.update_many({'activo': False}, {'$set': {True}})
    print(f'Usuarios actualizados: {res.modified_count}')



# -------------------------------------------------
# 13. ELIMINAR UNO
# -------------------------------------------------
def eliminar():

    nombre = input("Nombre a eliminar: ")

    # TODO: Eliminar usuario por nombre
    res = coll.delete_one({'nombre': nombre})
    if res.deleted_count == 1:
        print('\nEliminado correctamente.')
    else:
        print('\nNo se eliminó ningún usuario.')


# -------------------------------------------------
# 14. ELIMINAR VARIOS (POR EDAD)
# -------------------------------------------------
def eliminar_varios():

    edad = int(input("Eliminar usuarios menores a edad: "))

    # TODO: Eliminar usuario menores a edad especifica
    res = coll.delete_many({'edad': {'$lt': edad}})

# -------------------------------------------------
# 15. LISTAR COLECCIONES
# -------------------------------------------------
def listar_colecciones():

    colecciones = db.list_collection_names()

    for coll in colecciones:
        print(coll)

# -------------------------------------------------
# 16. BORRAR COLECCIÓN
# -------------------------------------------------
def borrar_coleccion():

    nombre = input("Nombre colección: ")


    db.drop_collection(nombre)

    print("Colección eliminada")

    collection = db[input("Ingresa el nombre:")]
    collection.drop()
    print("Colección eliminada")
    
# -------------------------------------------------
# 17. BORRAR BASE DE DATOS
# -------------------------------------------------
def borrar_base_datos():

    confirm = input("¿Seguro? (si/no): ")

    if confirm.lower() == "si":
        # TODO: 
        client.drop_database("mi_base")
        print("Base eliminada")


# -------------------------------------------------
# MENÚ PRINCIPAL
# -------------------------------------------------
def menu():
    while True:
        print("""
========= MENÚ PyMongo =========
1. Insertar
2. Insertar varios
3. Mostrar todos
4. Buscar por edad
5. Buscar activos
6. Buscar por ciudad
7. Buscar con proyección
8. Buscar uno
9. Contar documentos
10. Valores distintos
11. Actualizar rol
12. Activar usuarios inactivos
13. Eliminar uno
14. Eliminar varios (por edad)
15. Listar colecciones
16. Borrar colección
17. Borrar base de datos
0. Salir
""")

        opcion = input("Opción: ")

        if opcion == "1":
            insertar()
        elif opcion == "2":
            insertar_varios()
        elif opcion == "3":
            mostrar_todos()
        elif opcion == "4":
            buscar_con_filtro()
        elif opcion == "5":
            buscar_activos()
        elif opcion == "6":
            buscar_por_ciudad()
        elif opcion == "7":
            buscar_con_proyeccion()
        elif opcion == "8":
            buscar_uno()
        elif opcion == "9":
            contar()
        elif opcion == "11":
            actualizar()
        elif opcion == "12":
            actualizar_varios()
        elif opcion == "13":
            eliminar()
        elif opcion == "14":
            eliminar_varios()
        elif opcion == "15":
            listar_colecciones()
        elif opcion == "16":
            borrar_coleccion()
        elif opcion == "17":
            borrar_base_datos()
        elif opcion == "0":
            print("Saliendo")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()