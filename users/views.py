

# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:  # If authentication is successful
            login(request, user)  # Log the user in
            return redirect('welcome')  # Redirect to the welcome page
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})

    return render(request, 'users/login.html')

def welcome_view(request):
    return render(request, 'users/welcome.html')  # Render the welcome page
    
from django.shortcuts import render

def login_view(request):
    return render(request, 'users/login.html')

