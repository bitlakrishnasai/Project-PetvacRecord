from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):

    mydict={"hi":" from viwes.py"}
    return render(request,"index.html",mydict)
    
    #return HttpResponse("index.html")

def login(request):
    return render(request,"login.html")

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



    