
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from student1.forms import StudentRegistration
from . models import User

# Create your views here.


# this function for adding and displaying data
def home(request):
    
    if request.method == "POST":

        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nam=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']

            print(nam)
            print(em)
            print(ps)
            fm.save()
           
            # user=User(name=nam,email=em,password=ps)
            # user.save
           
    else:
          
            fm=StudentRegistration()

    stud=User.objects.all()
          
    return render(request,'stud1/stud1.html',{'form':fm,'stu':stud})

def delete(request,id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')

def update(request,id):
    if request.method =='POST':
        p=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=p)
        if fm.is_valid():
            fm.save()

    else:
        p=User.objects.get(pk=id)
        fm=StudentRegistration(instance=p)
        
    return render(request,'stud1/update.html',{'form':fm})