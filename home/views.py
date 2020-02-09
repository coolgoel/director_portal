from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import internal_letter,external_letter
from .forms import *
# Create your views here.

def internal_creation_form(request):
    form = Internal_creation_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form' : form,
    }
    return render(request,'home/internal_form.html',context)

def external_creation_form(request):
    form = External_creation_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form' : form,
    }
    return render(request,'home/external_form.html',context)

def edit_external(request,letter_id):
    if request.method == 'POST':

        letter = external_letter.objects.get(pk=letter_id) 
        form = External_creation_form(request.POST or None,instance=letter)
        if(form.is_valid()):            
            form.save()
            # messages.success(request,"Item has been Edited!")
            return redirect('dashboard')
    else:        
        letter = external_letter.objects.get(pk=letter_id) 
        form = External_creation_form(instance=letter)
        return render(request,'home/edit_external.html',{'form':form})

def edit_internal(request,letter_id):
    if request.method == 'POST':

        letter = internal_letter.objects.get(pk=letter_id) 
        form = Internal_creation_form(request.POST or None,instance=letter)
        if(form.is_valid()):            
            form.save()
            # messages.success(request,"Item has been Edited!")
            return redirect('dashboard')
    else:        
        letter = internal_letter.objects.get(pk=letter_id) 
        form = Internal_creation_form(instance=letter)
        return render(request,'home/edit_internal.html',{'form':form})

def user_login(request):
    if request.user.is_active:
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('dashboard'))

                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return HttpResponse("Invalid login details given")
        else:
            return render(request, 'home/login.html', {})

def dashboard(request):
    if request.user.is_active:
        for letters in internal_letter.objects.all():
            print(letters.si_no)
            print('\n')
        return render(request,'home/dashboard.html',
                              {'user_info':request.user,
                              'external_letters':external_letter.objects.all().order_by('si_no'),
                              'internal_letters':internal_letter.objects.all().order_by('si_no'),})
    else:
        return HttpResponseRedirect(reverse('user_login'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))
