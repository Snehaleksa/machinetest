from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User


# Create your views here.
def register(request):
   if request.method=='POST':
      firstname=request.POST['firstname']
      lastname=request.POST['lastname']
      email=request.POST['email']
      department=request.POST['department']
      designation=request.POST['designation']
      date=request.POST['date']
      salary=request.POST['salary']
      image=request.FILES.get('image')
      
      data=User.objects.create(firstname=firstname,lastname=lastname,email=email,department=department,designation=designation,date=date,salary=salary,image=image)
      data.save()
      return HttpResponse("success")
   else:
      return render(request,'register.html') 


def userhome(request):
   data=User.objects.all()
   return render(request,'userhome.html',{'data':data})  

def edit(request,id):
   data=User.objects.get(id=id)
   if request.method=='POST':
      data.firstname=request.POST['firstname']  
      data.lastname=request.POST['lastname']
      data.email=request.POST['email']
      data.department=request.POST['department']
      data.designation=request.POST['designation']
      data.date=request.POST['date']
      data.salary=request.POST['salary']
      if 'image' in request.FILES:
         data.image=request.FILES['image']
      data.save()
      return redirect(userhome)
   else:
      return render(request,'edit.html',{'data':data})
        
def search(request):
    if request.method=='POST':
        search=request.POST.get('search')
        data=User.objects.filter(firstname__icontains=search)
        return render(request,'userhome.html',{'data':data})
    
def delete(request,id):
   data=User.objects.get(id=id)
   data.delete()  
   return redirect(userhome)  

def profileview(request,id):
   data=User.objects.get(id=id)
   return render(request,'profileview.html',{'data':data})