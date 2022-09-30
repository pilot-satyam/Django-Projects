import imp
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST) ----> Using the existing template
        form = RegisterForm(request.POST)    # ----> Using our self created template instead
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, Aapka account ban chuka hai yaha')
            #return redirect('food:index')
            return redirect('login') # to redirect to login page after successful registration
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form}) #this code connects with the register.html file

@login_required #using this decorator so that after logging out, user is not redirected to blank page upon clicking back
def profilepage(request):
    return render(request,'users/profile.html')
