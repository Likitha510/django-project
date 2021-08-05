from django.shortcuts import render
from .models import info
def home(request):
    if request.method == 'POST':
        FIRSTNAME=request.POST['fname']
        LASTNAME=request.POST['lname']
        email=request.POST['EMAIL']
        Date=request.POST['dob']
        height=request.POST['height']
        weight=request.POST['weight']
        a=info(Firstname=FIRSTNAME,Lastname=LASTNAME,email=email,date=Date,height=height,weight=weight)
        a.save()
        c=(int(weight)/(int(height)/100))**2
        if c <= 16:
            d="You are underweight."
            return render (request,"santhu/login.html",{"d":d})
        elif c >= 18 and 25 >= c:
            d="You are healthy."
            return render(request,"santhu/login.html",{"d":d})

        else :
            d="you are overweight"
            return render(request, "santhu/login.html", {"d": d})
    else:
        return render(request,'santhu/index.html')

# Create your views here.