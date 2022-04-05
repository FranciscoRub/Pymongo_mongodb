from pymongo import MongoClient
import pprint
import random as rd
client = MongoClient("mongodb://localhost:27017")

db= client.Myslangs
Slangs = db.Slangs

#Slangs4 = {
 #   "ID": "4",
  #  "Slang": "Cool",
   # "Significado": "Aprobacion o señalar algo que esta de moda"
    #}

#resultado = Slangs.insert_one(Slangs4)
#print("Slang: "+ str(resultado.inserted_id))

#Slangs5 = {
 #   "ID": "5",
  #  "Slang": "Mopri",
   # "Significado": "Amigo cercano"
   # }
#Slangs6 = {
 #   "ID": "6",
  #  "Slang": "Ayala vida",
   # "Significado": "Queja o cuando sucede algo en un momento inoportuno"
   # }
#resultado_multiple = Slangs.insert_many([Slangs5,Slangs6])
#print("Slang: "+str(resultado_multiple.Slang6 = input("Nuevo slang: ")

#for Slang in Slangs.find():
 #   pprint.pprint(Slang)


def ver_diccionario():
    for Slang in Slangs.find():
         pprint.pprint(Slang)
def Crear_registro():
    
     print("----Crear Slang----")
     SlangX = input("Inserte Slang: ")
     SignificadoX = input("Inserte significado: ")
     ide = str(rd.randint(7,30))
     resultado = Slangs.insert_one({"ID": ide , "Slang": SlangX , "Significado": SignificadoX})
     ver_diccionario()
def editar_registros():
    ver_diccionario()
    ides = input("ID de palabra a editar: ")
    resultado = Slangs.find({"ID": ides})
    print("\n-----SELECCION-----")
    for r in resultado:
        print(r)
    slang = input("\n Nuevo slang: ")
    significado = input("significado: ")
    Slangs.update_one({"ID": ides},
                      {"$set":{"Slang": slang , "Significado": significado}})

    ver_diccionario()
def  eliminar_registro():
    ver_diccionario()
    ides = input("ID de palabra a eliminar: ")
    Slangs.delete_one({"ID": ides})
    ver_diccionario()
    
def mostrarslangs():
    resultado = Slangs.find({"Slang": "1"},{"ID":0,"Significado":0})
    for Slang in resultado:
        print(Slang)
    
print("--------------------------Diccionario de Slang Panameño-------------------------")
menuprincipal = int(input("--Menú Principal: \n 1- agregar nueva palabra \n 2- Editar palabra existente\n 3- Eliminar palabra existente \n 4- Ver listado de palabras \n 5- Buscar significado de palabra \n 6- Salir \n Elija una opción: "))
    

while menuprincipal !=6:
        
        
    if menuprincipal == 1:
        Crear_registro()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal == 2:
        editar_registros()
        editar_registros()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal == 3:
        eliminar_registro()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal ==4:
        ver_diccionario()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal ==5:
        mostrarslangs()
        menuprincipal==input("preciones Enter para seguir: ")
    else:
        print("Por favor digite una opción válida")
        
    menuprincipal = int(input("\n\n\nMenú Principal: \n 1- agregar nueva palabra \n 2- Editar palabra existente \n 3- Eliminar palabra existente \n 4- Ver listado de palabras \n 5- Buscar significado de palabra \n 6- Salir \n"))
client.close()

    
   
