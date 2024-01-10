from math import ceil
from django.shortcuts import render
from petapp.models import contact1
from django.contrib import messages
from petapp.models import product1

# Create your views here.
def base(request):
    return render(request,"petapp/base.html")
def home(request):
    allProds=[]                                             # this is a list
    catprods=product1.objects.values('category','id')       # list of objects/queryset-catprods 
    cats={item['category'] for item in catprods}            # This is a set-to extract unique categ of produc                           
    for cat in cats:    
        prod = product1.objects.filter(category=cat)
        n=len(prod)
        nSlides=n // 4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params= {"allProds": allProds}
    return render(request,"petapp/index.html", params)

def copy(request):
    return render(request,"petapp/copy.html")
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email") 
        desc=request.POST.get("desc")
        phone=request.POST.get("phone")
        myquery=contact1(name=name,email=email,desc=desc,phone=phone)
        myquery.save()

        messages.info(request,"We Will get back with you soon...")
    return render(request,"petapp/contact.html")

def checkout(request):
    return render(request,"petapp/checkout.html")


 

