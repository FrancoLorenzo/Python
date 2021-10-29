#!/usr/bin/env python
# coding: utf-8

# # Programacion orientada a Objetos

# In[1]:


class GrupoAnimal:
    x = 0
    def __init__(self):
        print('Estoy construido')

    def grupo(self) :
        self.x = self.x + 1
        print('Hasta ahora',self.x)

    def __del__(self):
        print('Estoy destruido', self.x)


# In[2]:


an = GrupoAnimal()
an.grupo()
an.grupo()
an = 42
print('an contiene',an)


# In[3]:


class GrupoAnimal:
    x = 0
    nombre = ''
    
    def __init__(self, nom):
        self.nombre = nom
        print(self.nombre,'construido')

    def grupo(self) :
        self.x = self.x + 1
        print(self.nombre,'recuento grupal',self.x)


# In[4]:


s = GrupoAnimal('Sally')
j = GrupoAnimal('Jim')
s.grupo()
j.grupo()
s.grupo()


# ## Herencia

# In[24]:


# Definimos una clase padre
class Animal:
    def __init__(self, especie, edad, patas):
        self.especie = especie
        self.edad = edad
        self.patas = patas
    
    def moverse(self):
        print(f"Caminando con {self.patas} patas")
    
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

# Creamos una clase hija que hereda de la padre
class Perro(Animal):
    def __init__(self, especie, edad, patas, propietario):
        super().__init__(especie, edad, patas)
        self.propietario = propietario


# In[19]:


print(Perro.__bases__)


# In[25]:


mi_perro = Perro('mamífero', 10, 4, 'Maria')
mi_perro.describeme()
mi_perro.moverse()
mi_perro.edad
mi_perro.propietario


# ### Herencia multiple

# In[26]:


class Clase1:
    pass
class Clase2(Clase1):
    pass
class Clase3(Clase2):
    pass


# In[27]:


print(Clase3.__bases__)


# In[28]:


class Clase1:
    pass
class Clase2:
    pass
class Clase3(Clase1, Clase2):
    pass


# In[29]:


print(Clase3.__mro__)

