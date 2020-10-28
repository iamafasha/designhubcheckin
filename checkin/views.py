from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,logout ,login
from django.http import HttpResponse
from .forms import LoginForm, AddForm
from .models import Visitors, Checkins
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        add_form = AddForm()
        visitors_list = Checkins.objects.all().order_by('-created_date')
        return render(
            request, 'checkin/mainpage.html', {
                    'addform': add_form,
                    'visitors_list': visitors_list
                })
    else:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request,username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.add_message(request, messages.ERROR,
                                        'Password might not be okay.')
        context = {"form": form}
        return render(request, 'checkin/index.html', context)

def checkin(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            temperature = form.cleaned_data.get('temperature')
            name = form.cleaned_data.get('name')
            company = form.cleaned_data.get('company')
            identification_number = form.cleaned_data.get('identification_number')
            telephone_number = form.cleaned_data.get('telephone_number')
            visitor = Visitors(name=name, company=company, identification_number=identification_number,telephone_number=telephone_number)
            visitor.save()
            registered_visitor = Checkins(visitor=visitor, temperature=temperature)
            registered_visitor.save()
    return redirect('index')


def recheckin(request):
    if request.method == 'POST':
        messages.add_message(request, messages.SUCCESS,'Added A new User.')
        temp=request.POST.get("temp")
        user_id=request.POST.get("visitor_id")
        print(user_id)
        visitor = Visitors.objects.get(pk=user_id)
        if visitor is not None:
            registered_visitor = Checkins(visitor=visitor, temperature=temp)
            registered_visitor.save()
    return redirect('index')
def logout_view(request):
    logout(request)
    return redirect('index')
