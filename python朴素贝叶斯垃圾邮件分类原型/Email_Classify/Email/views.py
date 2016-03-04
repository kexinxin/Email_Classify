from django.shortcuts import render
from models import Person,Email
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from _ast import Param
from django.dispatch.dispatcher import receiver
import BayesClassifier
# Create your views here.
def login(request):
    #Person.objects.create(name="WeizhongTu",password='kdfd')
    return render(request, 'login.htm')
def recieve(request):
    username=request.session['username']
    emails=[]
    emails=Email.objects.filter(receiver=username)
    return render(request,'recieve.htm',{'username':username,'emails':emails})

def write(request):
    username=request.session['username'] 
    return render(request,'write.htm',{'username':username})

def biz(request):
    username=request.session['username']
    emails=[]
    emails=Email.objects.filter(flag='businise',receiver=username)
    return render(request,'biz.htm',{'username':username,'emails':emails})
def pe(request):
    username=request.session['username']
    emails=[]
    emails=Email.objects.filter(flag='PE',receiver=username)
    return render(request,'pe.htm',{'username':username,'emails':emails})
def rubbish(request):
    username=request.session['username']
    emails=[]
    emails=Email.objects.filter(flag='travel',receiver=username)
    return render(request,'rubbish.htm',{'username':username,'emails':emails})
def send(request):
    username=request.session['username']
    emails=[]
    emails=Email.objects.filter(sender=username)
    return render(request,'send.htm',{'username':username,'emails':emails})
def world(request):
    username=request.session['username']
    emails=[]
    emails=Email.objects.filter(flag='health',receiver=username)
    return render(request,'world.htm',{'username':username,'emails':emails})
@csrf_exempt
def main(request):
    username = request.POST.get('userName')
    passWord = request.POST.get('userPWD')
    try:
        Person.objects.get(name=username,password=passWord)
        request.session['username'] = username
        emails=[]
        emails=Email.objects.filter(receiver=username)
        return render(request,'recieve.htm',{'username':username,'emails':emails})
    except ObjectDoesNotExist:
        return render(request, 'login.htm')
def logout(request):
    del request.session['username']
    return render(request, 'login.htm')
def sendOk(request):
    username=request.session['username']
    receiver=request.POST.get('receiver')
    theme=request.POST.get('theme')
    message=request.POST.get('message')
    flag=BayesClassifier.getClassify(message)
    Email.objects.create(sender=username,receiver=receiver,theme=theme,message=message,flag=flag)
    emails=[]
    emails=Email.objects.filter(sender=username)
    return render(request,'send.htm',{'username':username,'emails':emails})
def deleSendEail(request,parama):
    Email.objects.get(id=parama).delete()
    username=request.session['username']
    emails=[]
    emails=Email.objects.filter(sender=username)
    return render(request,'send.htm',{'username':username,'emails':emails})
def deleReceiverEail(request,parama):
    Email.objects.get(id=parama).delete()
    username=request.session['username']
    emails=[]
    emails=Email.objects.filter(receiver=username)
    return render(request,'recieve.htm',{'username':username,'emails':emails})
def deleBizEail(request,parama):
    Email.objects.get(id=parama).delete()
    username=request.session['username']
    emails=[]
    emails=Email.objects.filter(receiver=username,flag='biz')
    return render(request,'biz.htm',{'username':username,'emails':emails})
def delePeEail(request,parama):
    Email.objects.get(id=parama).delete()
    username=request.session['username']
    emails=[]
    emails=Email.objects.filter(receiver=username,flag='pe')
    return render(request,'pe.htm',{'username':username,'emails':emails})
def deleRubbishEail(request,parama):
    Email.objects.get(id=parama).delete()
    username=request.session['username']
    emails=[]
    emails=Email.objects.filter(receiver=username,flag='rubbish')
    return render(request,'rubbish.htm',{'username':username,'emails':emails})
def deleWorldEail(request,parama):
    Email.objects.get(id=parama).delete()
    username=request.session['username']
    emails=[]
    emails=Email.objects.filter(receiver=username,flag='world')
    return render(request,'world.htm',{'username':username,'emails':emails})
def viewContext(request,parama):
    email=Email.objects.get(id=parama)
    username=request.session['username']
    return render(request,'viewContext.htm',{'username':username,'email':email})
