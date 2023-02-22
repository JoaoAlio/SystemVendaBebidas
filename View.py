from tkinter import *
from tkinter import Tk
import mysql.connector

#Conexao com o banco de dados Mysql
conexao = mysql.connector.connect(
   host="localhost",
   user="root",
   password="1234567",
   database="System1"
)


