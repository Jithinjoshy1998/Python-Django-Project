from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm

# Create your views here.
def index(request):
    numbers={
        'num1':[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,'index.html',numbers)

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)

from django.shortcuts import render
from django.http import HttpResponse

def submit_contact_form(request):
    if request.method == 'POST':
        # Process form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # You can perform further processing, such as saving the data to a database
        
        # For now, let's just return a simple response
        return HttpResponse("Form submitted successfully!")
    else:
        # Handle GET request (if necessary)
        return HttpResponse("Method not allowed")

