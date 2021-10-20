from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):

     
    loggedin={"user":request.POST['user'],"csrf":request.POST['csrfmiddlewaretoken']}
    print(loggedin["csrf"])  
    
    mydict={"user":request.POST['user']}
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



    