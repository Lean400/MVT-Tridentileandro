from django.shortcuts import render
from django.http import HttpResponse
from AppFlia.models import Familia
from django.template import loader
#Importo render, HttpResonse, clase familia y loader para el HTML

def flia_db(request): #Datos que completan la BD (de la clase Familia)
    mimujer = Familia(nombre = "Zomerlys Ponce", fecha_nacim ="1992-01-23", dni = 23432145)

    mimadre = Familia(nombre = "Norma Gorosito", fecha_nacim = "1968-07-06", dni = 34567654)

    mihermano = Familia(nombre = "Alan Tridenti", fecha_nacim = "1996-02-07", dni = 23453656)

    mimujer.save()
    mimadre.save()
    mihermano.save()   
    #Guardo los cambios en variables

    

    dic = {
        "nombre_mimujer": mimujer.nombre,
        "fechanacim_mimujer": mimujer.fecha_nacim,
        "dni_mimujer": mimujer.dni,
        "nombre_mimadre": mimadre.nombre,
        "fechanacim_mimadre": mimadre.fecha_nacim,
        "dni_mimadre": mimadre.dni,        
        "nombre_mihermano": mihermano.nombre,
        "fechanacim_mihermano": mihermano.fecha_nacim,
        "dni_mihermano": mihermano.dni
        }
    #Diccionario del cual se van a sacar los datos para el HTML (Voy a usar la clave siempre)
    
    plantilla = loader.get_template("template1.html") #Llamo al template (Ojo con el nombre)
    doc = plantilla.render(dic)

    return HttpResponse(doc) #Documento que va a devolver
    





