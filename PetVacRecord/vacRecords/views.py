from django.shortcuts import render,HttpResponse
from datetime import datetime
from vacRecords.models import User

# Create your views here.

def index(request):

     
    loggedin={"user":request.POST['user'],"csrf":request.POST['csrfmiddlewaretoken']}
    print(loggedin["csrf"])  
    
    mydict={"user":request.POST['user']}
    return render(request,"index.html",mydict)
    
    #return HttpResponse("index.html")

def login(request):

    return render(request,"login.html")



def signUp(request):
        print(request.POST)
    
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneNumber=str(request.POST.get('phnumber'))
        password=request.POST.get('password')
        date=datetime.today()

        user=User(name=name,email=email,phoneNumber=phoneNumber,password=password,date=date)

        user.save()


        
    # user=True
    # if user==True:
    #     signup={"message":"Your have signed up successfully. Please login to continue."}


    #     return render(request,'login.html',signup)

    # else:

    #     signup={"message":"User already exists.Please use a different username or sign in if you are already a member."}


        return render(request,'login.html')



def addVacRecord():
    pass

def editRecord():
    pass

def delVacRecord():
    pass

def addPet():
    pass

def removePet():
    pass

def reminder():
    pass



    