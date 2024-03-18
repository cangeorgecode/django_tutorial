# Steps to create login function in Django

1. In app/urls.py, add
```path('login/', views.login_user, name='login_user'),```
2. In app/views.py, add
```from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'core/index.html')

def login_user(request):
    # If request is POST. If form is valid, login
    # If request is GET, show login form
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('index')
        else:
            messages.success(request, 'There was an error logging in, please try again!')
    else:
        return render(request, 'core/login.html', {})
```
3. Create a login.html template
4. If there's a homepage, make sure to change the href to the login in the homepage
5. To logout, in views.py, add
```
def logout_user(request):
    logout(request)
    messages.success(request, 'See ya!')
    return redirect('home') # Make sure the redirect path exists
```
6. In app/urls.py, add
```
 path('logout/', views.logout_user, name='logout_user'),
```
7. No need to add a logout HTML template

