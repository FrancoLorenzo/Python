#!/usr/bin/env python
# coding: utf-8

# # Modulos

# In[1]:


import os


# In[5]:


os.getcwd()


# In[6]:


os.makedirs('C:\\Users\\Maricel\\Desktop\\Python-Basico\\Sesion 06\\PruebaOS')


# In[7]:


path = 'C:\\Users\\Maricel\\Desktop\\Python-Basico\\Sesion 06\\PruebaOS\\setup.py'


# In[8]:


os.path.basename(path)


# In[9]:


os.path.dirname(path)


# In[10]:


os.path.getsize(path)


# In[13]:


print(os.path.exists('C:\\Windows'))
print(os.path.exists('C:\\some_made_up_folder'))
print(os.path.isdir('C:\\Windows\\System32'))
print(os.path.isfile('C:\\Windows\\System32'))
print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))
print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))


# In[14]:


import sys


# In[15]:


print(sys.argv)


# In[16]:


sys.path


# In[17]:


sys.version


# In[18]:


import webbrowser


# In[19]:


webbrowser.open("http://www.python.org", new=2, autoraise=True)


# In[21]:


webbrowser.open_new("https://pypi.python.org/pypi")


# In[22]:


webbrowser.open_new_tab("https://www.python.org/psf-landing/")


# In[26]:


comando = "/usr/bin/firefox %s"
nav3 = webbrowser.get(comando)
webbrowser.register("navegador", None, nav3)
webbrowser.get("navegador").open("http://www.python.org")


# In[27]:


browser = None
browsers = ("firefox", "opera", "mosaic", None)
for b in browsers:
    try:
        browser = webbrowser.get(b)
    except webbrowser.Error:
        if b is None:
            print("No hay navegador registrado.")
        else:
            print("No se ha encontrado '%s'." % b)
    else:
        if b is None:
            print("Navegador por defecto.")
        else:
            print("Navegador '%s'." % b)


# In[29]:


webbrowser.open_new_tab("http://www.recursospython.com/")
# Abrir una nueva ventana en Chrome
try:
    webbrowser.get("chrome").open_new("http://www.recursospython.com/")
except webbrowser.Error:
    print("No se ha encontrado Chrome.")

