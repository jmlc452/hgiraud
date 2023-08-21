from django.shortcuts import render,redirect
from django.http import HttpResponse
import smtplib

# Create your views here.

def index(request):
    if(request.method=="POST"):
        nombre = request.POST.get("name")
        email = request.POST.get("email")
        contenido = request.POST.get("message")
        asunto = request.POST.get('subject')
        tlf=request.POST.get("phone")
        print(nombre,email,contenido,asunto,tlf)
        body = 'Subject: {}\n\n{}'.format(nombre, contenido,email)
        server = smtplib.SMTP('smtp.gmail.com','587')
        server.starttls()
        server.login('jmlc452@gmail.com','wpzsrvrahniskhii')
        server.sendmail(email,'jmlc452@gmail.com',  body + " by ")
        server.quit()
        return redirect("inicio")
    return render(request,'index.html')

def ingresar(request):
    return render(request,'ingresar.html')