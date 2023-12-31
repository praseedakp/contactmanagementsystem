from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import logout

# Create your views here.
def newpage(request):
    return render(request,'index.html')


#regview:
def regfunction(request):
    if request.method=='POST':
        a=regform(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['fname']
            ln=a.cleaned_data['lname']
            un=a.cleaned_data['image']
            em=a.cleaned_data['emailid']
            pho=a.cleaned_data['addr']
            fi=a.cleaned_data['contact']
            b=regmodel(fname=fn,lname=ln,image=un,emailid=em,addr=pho,contact=fi)
            b.save()
            return redirect(display)
        else:
            return HttpResponse("failed.... sorry... try again")

    return render(request,'register.html')


#display:
def display(request):
    k=regmodel.objects.all()
    id1=[]
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    for i in k:
        id2=i.id
        id1.append(id2)
        p=i.fname
        a.append(p)
        q=i.lname
        b.append(q)
        im=str(i.image).split('/')[-1]
        c.append(im)
        pd=i.emailid
        d.append(pd)
        cp=i.addr
        e.append(cp)
        cs=i.contact
        f.append(cs)
    p=zip(id1,a,b,c,d,e,f)
    return render(request,'indexone.html',{'p':p})



#delete:
def delete(request,id):
    a=regmodel.objects.get(id=id)
    os.remove(str(a.image))
    a.delete()
    return redirect(display)


# editcode for admin productpage
def edit(request,id):
    a=regmodel.objects.get(id=id)
    img=str(a.image).split('/')[-1]
    if request.method=='POST':
        a.fname=request.POST.get('fname')
        a.lname=request.POST.get('lname')
        a.emailid=request.POST.get('emailid')
        a.addr=request.POST.get('addr')
        a.contact=request.POST.get('contact')
        if len(request.FILES)!=0:
            if len(a.image)>0:
                os.remove(a.image.path)
            a.image=request.FILES['image']
        a.save()
        return redirect(display)
    return render(request,'edit.html',{'a':a,'img':img})
