from django.contrib import messages
from django.shortcuts import render, redirect

from opelka.forms import FormDataForm
from opelka.models import FormData


# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request.POST)
        form = FormDataForm(request.POST)

        print(form.is_valid())

        if form.is_valid():
            form.save()
            messages.success(request, 'Information saved successfully.')
            return redirect('index')
    else:
        form = FormDataForm()
    return render(request, 'auth/index.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'opelka' and password == 'opelka':
            # Authentication successful, redirect to home page or wherever you want
            return redirect('index')  # Assuming you have a URL named 'home' defined
        else:
            # Authentication failed, render the login page with an error message
            return render(request, 'auth/login.html', {'error': 'Invalid username or password'})
    return render(request, 'auth/login.html')


def upload_information(request):
    uploaded_information = FormData.objects.all()  # Retrieve all uploaded information
    return render(request, 'auth/upload_information.html', {'uploaded_information': uploaded_information})
