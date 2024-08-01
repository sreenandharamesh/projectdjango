from django.shortcuts import render,redirect
from userapp.models import User

# Create your views here.
def home_page_view(request):
    return render(request,'home.html',context = {})

def add_user_view(request):
    return render(request,'add_user.html',context= {})

def save_user_view(request):
    if request.method == 'POST':
        # Retrieve form data and create a new student record
        name = request.POST['name']
        title = request.POST['title']
        content = request.POST['content']
        date = request.POST['date']
      
        print("Name: ", name)
        print("Title: ", title)
        print("content: ", content)
        print("date:", date)

        user = User(name=name, title=title, content=content , date=date)
        user.save()
        return redirect('add')
def get_all_users(request):    
    user =User.objects.all()
    context ={
        'allusers': user

    }
    return render(request,'allusers.html',context=context)

def delete_user_view(request,user_id):
    user =User.objects.filter(pk = user_id)
    user.delete()
    return redirect('all')

def get_user_info(request,user_id):
    user =User.objects.get(pk = user_id)
    context ={
        'user':user
    }
    return render(request ,'get_user_info.html',context=context)

def update_user(request,user_id):
 user =User.objects.get(pk = user_id)

 user.name = request.POST['name']
 user.title = request.POST['title']
 user.content = request.POST['content']
 user.date = request.POST['date']

 user.save()
 return redirect('all')