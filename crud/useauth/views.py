from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def homepage(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return render(request, 'useauth/signup.html',{'message':"Your Account has been sucessfully created"})
    return render(request,'useauth/signup.html')