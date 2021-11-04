#!/usr/bin/env python
# coding: utf-8

# # Manipulacion de archivos

# In[1]:


manejador_archivo = open('mbox.txt')
print(manejador_archivo)


# In[2]:


#Falla del archivo
manejador_archivo = open('stuff.txt')


# In[3]:


man_archivo = open('mbox-short.txt')
contador = 0
for linea in man_archivo:
    contador = contador + 1
print('Contador de líneas:', contador)


# In[4]:


manejador_archivo = open('mbox-short.txt')
inp = manejador_archivo.read()
print(len(inp))
print(inp[:20])


# In[7]:


man_a = open('mbox-short.txt')
contador = 0
for linea in man_a:
    linea = linea.rstrip() # Elimina los espacios en blanco del lado derecho de la cadena
    if linea.startswith('From:'):
        print(linea)


# In[8]:


man_a = open('mbox-short.txt')
for linea in man_a:
    linea = linea.rstrip()
    # Ignorar lineas que no nos interesan
    if not linea.startswith('From:'):
        continue
    # Procesar la linea que nos 'interesa'
    print(linea)


# In[9]:


man_a = open('mbox-short.txt')
for linea in man_a:
    linea = linea.rstrip()
    if linea.find('@uct.ac.za') == -1: continue
    print(linea)


# In[10]:


narchivo = input('Ingresa un nombre de archivo: ')
man_a = open(narchivo)
contador = 0
for linea in man_a:
    if linea.startswith('Subject:'):
        contador = contador + 1
print('Hay', contador, 'lineas de asunto (subject) en', narchivo)


# In[12]:


narchivo = input('Ingresa un nombre de archivo: ')
try:
    man_a = open(narchivo)
except:
    print('No se puede abrir el archivo:', narchivo)
    exit()
contador = 0
for linea in man_a:
    if linea.startswith('Subject:'):
        contador = contador + 1
print('Hay', contador, 'lineas de asunto (subject) en', narchivo)


# In[1]:


fsal = open('salida.txt', 'w')
print(fsal)


# In[2]:


linea1 = "Aquí está el zarzo,\n"
fsal.write(linea1)
linea2 = 'el símbolo de nuestra tierra.\n'
fsal.write(linea2)
fsal.close()


# In[3]:


#Crear una nueva carpeta
import os
os.makedirs("Practica")


# In[4]:


#Listar el contenidos de una carpeta
os.listdir("./")


# In[5]:


#Mostrar el actual directorio de trabajo
os.getcwd()


# In[6]:


#Mostrar el tamaño del archivo en bytes del archivo pasado en parámetro
os.path.getsize("Practica")


# In[7]:


#¿Es un archivo el parámetro pasado?
os.path.isfile("Practica")


# In[8]:


#¿Es una carpeta el parámetro pasado?
os.path.isdir("Practica")


# In[10]:


#Renombrar un archivo
os.rename("Practica","PracticaV1")
os.listdir("./")


# In[11]:


#Eliminar un archivo
os.chdir("PracticaV1")
archivo = open(os.getcwd()+'/datos.txt', 'w')
archivo.write("Se Feliz!")
archivo.close()


# In[12]:


os.getcwd()
os.listdir("./")
os.remove(os.getcwd()+"/datos.txt")
os.listdir("./")

