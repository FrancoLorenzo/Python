#!/usr/bin/env python
# coding: utf-8

# # Gestion de diccionarios

# In[14]:


dic = dict(zip('abcd',[1,2,3,4]))
print(dic)


# In[16]:


items = dic.items()
print(items)


# In[17]:


keys= dic.keys()
print(keys)


# In[18]:


values= dic.values()
print(values)


# In[26]:


dic = dict.fromkeys(['a','b','c','d'],1)
print(dic)


# In[27]:


valor = dic.pop('b') 
print(valor)
print(dic)


# In[28]:


valor = dic.setdefault('e',5)
print(dic)


# In[1]:


palabra = "Bienvenidos al lenguaje Python"
diccionario = dict()


# In[4]:


for d in palabra:
    if d not in diccionario:
        diccionario[d] = 1
    else:
        diccionario[d] = diccionario[d] + 1
print(diccionario)


# In[5]:


diccionarioV2 = dict()
for c in palabra:
    diccionarioV2[c] = diccionarioV2.get(c, 0) + 1
print(diccionarioV2)


# In[9]:


contadores = { 'chuck' : 1 , 'annie' : 42, 'jhon': 100, 'jane': 5}
for clave in contadores:
    print(clave, contadores[clave])


# In[7]:


for clave in contadores:
    if contadores[clave] > 10 :
        print(clave, contadores[clave])


# In[10]:


lst = list(contadores.keys())
print(lst)
lst.sort()
for clave in lst:
    print(clave, contadores[clave])


# In[12]:


import string

fname = input('Ingresa el nombre de archivo: ')
try:
    fhand = open(fname)
except:
    print('El archivo no se puede abrir:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

