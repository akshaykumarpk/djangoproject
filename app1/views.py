from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import RegiterForms,LoginForm,UpdateForm,ChangePasswordForm,ImageForm
from.models import Register
from.models import Imagego
from django.contrib import messages
from django.contrib.auth import logout as logouts

# Create your views here.
def hello(request):
    return HttpResponse("hi")

def index(request):
    sub=67+90
    return render(request,'index.html',{'data':sub})

def register(request):
    if request.method=='POST':
        form=RegiterForms(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            Confirmpassword=form.cleaned_data['Confirmpassword']
            

            user=Register.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,"user already exists")
                return redirect('/register')

            elif password!=Confirmpassword:
                messages.warning(request,"password missmatch")
                return redirect('/register')
            else:
                tab=Register(Name=name,Age=age,Place=place,Email=email,Password=password)
                tab.save()
                messages.success(request,"registration sucsessful")
                return redirect('/')
    else:
        form=RegiterForms()
    return render(request,'register.html',{'data':form})


def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=Register.objects.get(Email=email)

                if not user:
                    messages.warning(request,"user does not  exists")
                    return redirect('/login')

                elif password!=user.Password:
                    messages.warning(request,"password incorrect")
                    return redirect('/login')
                else:
                    messages.success(request,"login sucsessful")
                    return redirect('/home/%s' % user.id)
            except:
                messages.warning(request,"incorrect")
                return redirect('/login')
    else:
        form=LoginForm()
    return render(request,'login.html',{'data':form})
def home(request,id):
    user=Register.objects.get(id=id)
    return render(request,'home.html',{'user':user})
def showusers(request):
    users=Register.objects.all()
    return render(request,'showusers.html',{'users':users})

def delete(request,id):
    user=Register.objects.get(id=id)
    user.delete()
    messages.success(request,"delete succesful")
    return redirect('/showusers')

def update(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"update success")
            return redirect('/showusers')
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'user':user,'form':form})
def changepassword(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']
        if user.Password!=oldpassword:
            messages.warning(request,"password incorrect")
            return redirect('/showusers')
        elif oldpassword==newpassword:
            messages.warning(request,"password already exists")
            return redirect('/showusers')
        elif newpassword!=confirmpassword:
            messages.warning(request,"password missmatch")
            return redirect('/showusers')
        else:
            user.Password=newpassword
            user.save()
            messages.success(request,"success")
            return redirect('/home/%s' % user.id)
    else:
        form=ChangePasswordForm()
    return render(request,'changepassword.html',{'user':user,'form':form})
def image(request):
    if request.method=='POST':
        form=ImageForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"successful")
            return redirect('/')
    else:
        form=ImageForm()
    return render(request,'image.html',{'form':form})     
def gallery(request):
    images=Imagego.objects.all()
    return render(request,'gallery.html',{'images':images})
def logout(request):
    logouts(request)
    messages.success(request,"logout success")
    return redirect('/')
def showdetails(request):
    detail=Imagego.objects.all()
    return render(request,'showdetails.html',{'detail':detail})