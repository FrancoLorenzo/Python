#!/usr/bin/env python
# coding: utf-8

# In[1]:


from calculos.utilidades import calculos
from calculos.utilidades.impuestos import impuesto_iva14


# In[2]:


monto = int(input("Introduzca un monto entero: "))
monto_suma = int(input("Introduzca un monto entero a sumar: "))


# In[3]:


suma = impuesto_iva14(monto) + calculos.suma_total(monto_suma)


# In[8]:


print("Total a Facturar: {0} colones, con IVA 14%.".format(suma))


# # Instalación del paquete

# In[ ]:


#Abrir en el command o terminal la ruta donde se encuentra el paquete
#python setup.py sdist


# In[7]:


pip install dist\\calculos-0.1.tar.gz


# In[26]:


import calculos.utilidades.impuestos as imp
import calculos.utilidades.calculos as cal


# In[27]:


dir(cal)


# In[28]:


dir(imp)


# In[29]:


help(cal)


# In[30]:


help(imp)


# In[31]:


monto = int(input("Introduzca un monto entero: "))
monto_suma = int(input("Introduzca un monto entero a sumar: "))


# In[32]:


suma = imp.impuesto_iva14(monto) + cal.suma_total(monto_suma)


# In[33]:


print("Total a Facturar: {0} colones, con IVA 14%.".format(suma))


# In[6]:


#pip uninstall calculos

