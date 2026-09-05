from django.shortcuts import render,HttpResponse,redirect
from .models  import register as Register

# Create your views here.
def home(request):
    #return HttpResponse("I am home page")
    return render(request,"home.html")
def about(request):
    #return HttpResponse("I am about page")
    return render(request,"about.html")

def register(request):
    return render(request,"register.html")
def  formsave(request):
    if request.method=="POST":
        fn=request.POST["fullname"]
        em=request.POST["email"]
        ps=request.POST["password"]
        cn=request.POST["contact"]
        ad=request.POST["address"]
        r=Register(fullname=fn,email=em,password=ps,contact=cn,address=ad)
        r.save() #insert
   #return HttpResponse("succesfully register")
        return redirect("/viewdata")
    else:
        return redirect("/register")
        
    
        

def viewdata(request):
    data=Register.objects.all()
    return render(request,"viewdata.html",{'data':data})

def deletestudent(request,id):
    register.objects.filter(id=id).delete()
    return redirect("/ viewdata")

def updatestudent(request):
    id=request.GET["id"]
    data1=Register.objects.filter(id=id)
    return render(request,"update.html",{'data':data1})

def profileupdate(request):
    if request.method=="POST":
            id=request.POST["id"]
            fn=request.POST["fullname"]
            em=request.POST["email"]
            ps=request.POST["password"]
            cn=request.POST["contact"]
            ad=request.POST["address"]
            Register.objects.filter(id=id).update(fullname=fn,email=em,password=ps,contact=cn,address=ad)
            return redirect("/viewdata")
    else:
            return redirect("/register")
def login(request):
        return render(request,"login.html")

def logincheck(request):
    if request.method=="POST":
        em=request.POST["email"]
        ps=request.POST["password"]
        
        Register.objects.filter(email=em,password=ps)
        return redirect("/dashboard")
    else:
        return redirect("/login")
def dashboard(request):
    return render(request,"dashboard.html")
        

    
        
    
    