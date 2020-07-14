from django.shortcuts import render,redirect
from app18.models import Employee
from django.contrib import messages

def showIndex(request):
    return render(request,"index.html")

def addEmp(request):
    return render(request,"addEmp.html")

def saveEmp(request):
    idno=request.POST.get("t1")
    Name=request.POST.get("t2")
    City=request.POST.get("t3")
    Salary=request.POST.get("t4")

    Employee(idno=idno,Name=Name,City=City,Salary=Salary).save()

    messages.success(request,"Ragistration Successfull")
    return redirect("main")

def allEmp(request):
    res=Employee.objects.all()
    return render(request,"allEmp.html",{"data":res})

def deleteEmp(request):
    no=request.GET.get("no")
    Employee.objects.filter(idno=no).delete()
    return redirect('allEmp')

def show_update(request):
    no=request.GET.get("t1")
    result=Employee.objects.get(idno=no)
    return render(request,"update.html",{"data":result})

def update_emp(request):
    idno=request.POST.get("t1")
    Name=request.POST.get("t2")
    City=request.POST.get("t3")
    Salary=request.POST.get("t4")
    Employee.objects.filter(idno=idno).update(Name=Name,Salary=Salary,City=City)
    return redirect('allEmp')

