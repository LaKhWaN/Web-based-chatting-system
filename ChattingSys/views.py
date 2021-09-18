from django.shortcuts import redirect
from django.shortcuts import render
import mysql.connector as sql

mydb = sql.connect(host="localhost",user="root",passwd="",database="mysql")
mycursor = mydb.cursor()

def index(request):
    return render(request,'index.html')

def livechat(request):
    name = request.GET.get('name')
    clientName = request.GET.get('clientname')
    query = f"INSERT INTO chat(name,clientName) VALUES('{name}','{clientName}')"
    mycursor.execute(query)
    mydb.commit()
    mycursor.execute(f"SELECT clientMessage FROM chat WHERE clientName = '{clientName}'")
    clientMessage = mycursor.fetchall()
    print('\n\n!!!!!!!!')
    length = len(clientMessage)
    newClientMessage = clientMessage[length-1][0]
    params = {'clientName':clientName,'clientMessage':newClientMessage,'name':name}
    f = open("__cache__.txt","w")
    f.write(name)
    f.close()
    return render(request,'livechat.html',params)

def livechat2(request):
    msg = request.GET.get('message')
    clientMessage = "Null"
    clientName = "Null"
    f=open("__cache__.txt","r")
    name = f.read()
    f.close()
    params = {'clientName':clientName,'clientMessage':clientMessage,'name':name}
    return render(request,'livechat.html',params)