# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rnPeNc1T42hOr9XYDHt_Jlft5SgwHX2s
"""

username = 'Beril'
password = 'helloworld'
username1 = input('Enter your user name: ')
password1 = input('Enter your password: ')
if (username != username1 and password != password1):
  print('Invalid user name and password')
elif (username != username1 and password == password1):
  print('Invalid user name')
elif (username == username1 and password != password1):
  print('Invalid password')
else:
  print('You have successfully logged in!')

mydict = {'username':'Beril' , 'password':'helloworld'}
username1 = input('Enter your user name: ')
password1 = input('Enter your password: ')
if (username != username1 and password == password1):
  print('Invalid user name')
elif (username == username1 and password != password1):
  print('Invalid password')
elif (username != username1 and password != password1):
  print('Invalid user name and password')
else:
  print('You have successfully logged in!')