# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from auth.forms import UserForm
def login_user(request):
    """docstring for login_user"""
    state = 'Please log in beblow...'
    username = password = ''
    redirectUrl = request.GET.get('next')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                # redirect to success.html 
                url = request.POST.get('next')
                return HttpResponseRedirect(url)
            else:
                state = "Your account is not active, Please contact the site"
        else:
            state = "Your username and/or password were incorrect"

    return render_to_response('account/login.html', {
        'state':state,'username':username,'next':redirectUrl,
        }, context_instance=RequestContext(request)
    )

def register(request):
    """docstring for register"""
    nextUrl = request.GET.get('next')
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            # login after register
            new_user = authenticate(username=request.POST['username'],password=request.POST['password'])
            login(request, new_user)
            return HttpResponseRedirect(nextUrl)
    else:
        uf = UserForm()
    return render_to_response('account/register.html', {
            'next':nextUrl,
            'userform':uf
            },context_instance=RequestContext(request))
        

