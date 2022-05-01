import mysql.connector

dbcnct = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="")

mycursor = dbcnct.cursor()

# def usedatabase():
#     global dbcnct
#     dbcnct = mysql.connector.connect(host="localhost",
#                                      user="root",
#                                      password="",
#                                      database="BusFair")
#     global mycursor
#     mycursor = dbcnct.cursor()