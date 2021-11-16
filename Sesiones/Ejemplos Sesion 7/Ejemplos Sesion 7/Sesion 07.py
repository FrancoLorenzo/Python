#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
man = open('mbox-short.txt')
for linea in man:
    linea = linea.rstrip()
    if re.search('From:', linea):
        print(linea)


# In[3]:


# Usar el ^ hace que se retornen solamente las lineas que inicien con la palabra from
man = open('mbox-short.txt')
for linea in man:
    linea = linea.rstrip()
    if re.search('^From:', linea):
        print(linea)


# In[4]:


# Búsqueda de líneas que comiencen con 'F', seguidas de 2 caracteres, seguidos de 'm:'
man = open('mbox-short.txt')
for linea in man:
    linea = linea.rstrip()
    if re.search('^F..m:', linea):
        print(linea)


# In[6]:


# Devuelve coincidencias con líneas que empiecen con “From:”, seguidas de uno o más caracteres (.+), seguidas de un carácter @uct
man = open('mbox-short.txt')
for linea in man:
    linea = linea.rstrip()
    if re.search('^From:.+@uct', linea):
        print(linea)


# In[7]:


# Busca las frases que coincidan con tener cualquier caracter previo al @ y cualquier caracter despues del @
s = 'Una nota de csev@umich.edu a cwen@iupui.edu sobre una reunión @ 2PM'
lst = re.findall(r'\S+@\S+', s)
print(lst)


# In[8]:


man = open('mbox-short.txt')
for linea in man:
    linea = linea.rstrip()
    x = re.findall(r'\S+@\S+', linea)
    if len(x) > 0:
        print(x)


# In[9]:


man = open('mbox-short.txt')
for linea in man:
    linea = linea.rstrip()
    x = re.findall(r'[a-zA-Z0-9]\S+@\S+[a-zA-Z]', linea)
    if len(x) > 0:
        print(x)


# In[10]:


#Se extraen los datos que inicien con X-, seguido de 0 o mas caracteres, seguido de dos puntos, 
#luego de un espacio y una secuencia de uno o varios numeros
man = open('mbox-short.txt')
for linea in man:
    linea = linea.rstrip()
    if re.search(r'^X\S*: [0-9.]+', linea):
        print(linea)


# In[12]:


man = open('mbox-short.txt')
for linea in man:
    linea = linea.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', linea)
    if len(x) > 0:
        print(x)


# In[ ]:




