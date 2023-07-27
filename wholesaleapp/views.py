from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Representative
import bcrypt

# render login page
def log(request):
    request.session['logged']= False
    return render (request,'log.html')

# validate login and redirect to home page
def login(request):
    postData=request.POST
    errors = User.objects.login_validator(postData)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        users=User.objects.filter(email=request.POST['email'])
        logged_user=users[0]
        request.session['name']=f"{logged_user.name}"
        request.session['logged']=True
        request.session['id']=users.id
    return redirect ('/home')

def reg(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        User.objects.create (
            name= request.POST['name'],
            adress= request.POST['name'],
            phone_number= request.POST['phone_number']
            email= request.POST['email'],
            password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            )
    return redirect ('/')

def home(request):
    pass

# log out the site and delete all session data'
def logout(request):
    if request.method == 'POST':
        del request.session['loggedUser']
        request.session['logged']= False
        request.session.flush()
    return redirect ('/')

def companyform(request):
    return render (request,'companyform.html')

def createcompany(request):
    if request.method =='POST':
            name = request.POST['name'] 
            adress = request.POST['adress'] 
            telephone_number = request.POST['phonenum'] 
            email = request.POST['email']
            password = request.POST['password']
               
            User.objects.create(
                name = name,
                adress = adress,
                telephone_number = telephone_number ,
                email = email,
                password = password
            )
    return redirect('/signup') 
    
    

            
      
        


def salesrepform(request):
    if request.method =='POST':
            name = request.POST['repname'] 
            
            phone_no = request.POST['phone_number'] 
            email = request.POST['email']
            city = request.POST['city']
               
            Representative.objects.create(
                name = name,
                phone_no = phone_no,
                email = email,
                city = city,
                
            )
    return redirect('/salesrep')