#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tkn
        
ventana = tkn.Tk()
ventana.title("Proyecto Integrador")
ventana.config(width=400, height=300)

lista_alumnos3 = {}

caja_NA = tkn.Entry()
caja_NA.place(x=120, y=70, width=170, height=25)


caja_C = tkn.Entry()
caja_C.place(x=120, y=120, width=60, height=25)


def VerLista():
    print("Lista de alumnos:")

    #para cada fila de lista_alumno (para cada alumno) imprimo los 2 campos (0: Nombre, 1: Cant. materias), borro opción
    for k, v in lista_alumnos3.items():
        print("%s - %s cursos" %(k,v))

bot_VerLista = tkn.Button(text="Ver lista de alumnos", command=VerLista)
bot_VerLista.place(x=15, y=15, width=120, height=25)

et_NombrAlum = tkn.Label(text="Nombre alumno:")
et_NombrAlum.place(x=15, y=70)

et_Cursos = tkn.Label(text="Cursos:")
et_Cursos.place(x=15, y=120)

def ing_alum3():
    nombre=caja_NA.get()
    cursos=caja_C.get()
    
    #añado una nueva lista de 2 elementos (Nombre y Cantidad de Cursos) a la lista de alumnos
    lista_alumnos3.update({nombre:cursos})
    return lista_alumnos3

bot_AgList = tkn.Button(text="Agregar a la lista", command=ing_alum3)
bot_AgList.place(x=15, y=175, width=100, height=25)

def VerCursos():
    nombre=caja_NA.get()
    print("%s tiene %s cursos inscritos" %(nombre, lista_alumnos3[nombre]))

bot_VerCursos = tkn.Button(text="Ver cantidad de cursos", command=VerCursos)
bot_VerCursos.place(x=125, y=175, width=130, height=25)

ventana.mainloop()

