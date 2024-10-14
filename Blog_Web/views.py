from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login_r')
def blog(request):
    return render(request, 'blog.html')


def follow(request):
    #messages.info(request, 'You Follow Abid Hasan')
    return render(request, 'follow.html')


def blog_form(request):
    return render(request, 'form.html')


# Register Form -------------------------

def register(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        email = request.POST.get('email')
        passw = request.POST.get('password1')
        confirmpassw = request.POST.get('password2')
        
        if passw != confirmpassw:
            messages.error(request, 'Password Did not Mtach!')
            #return HttpResponseRedirect('/blog_r')
        
        elif len(email)<22:
            messages.error(request, 'Invalid Email, Please Enter Your Email at least 22 of Characters')
        
        elif len(usern)<4:
            messages.error(request, 'Please Enter Your Correct Username')

        elif User.objects.filter(username=usern).exists():
            messages.error(request, 'This User Already Exist')

        elif len(passw)<6:
            messages.error(request, 'Enter Password Almost 6 of Characters Number')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'This Email Already Exist')

        else:
            user_obj = User.objects.create_user(usern,email,passw)
            user_obj.save()
            messages.success(request, 'You are Successfully Sign Up, Please Login Here.....')
            return HttpResponseRedirect('/login_r')
        
    return render(request, 'register.html')


# login -----------------------------

def blog_login(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        passw = request.POST.get('password')

        user = authenticate(username=usern, password=passw)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/abid_blog')
        
        else:
            messages.error(request, 'Invalid Username or Password !')
            return HttpResponseRedirect('/login_r')
    
    else:
        return render(request, 'login.html')
    


def micro(request):
    return render(request, 'micro.html')