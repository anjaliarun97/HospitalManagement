from django.shortcuts import render
from .models import Department, Doctor
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    else:
        form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request, 'booking.html',{'form': form})



def doctor(request):
    doctors_list = Doctor.objects.all()
    context = {'doctors': doctors_list}
    return render(request, 'doctors.html', context)


def contact(request):
    return render(request, 'contact.html')


def department(request):
    departments_list = Department.objects.all()
    context = {'dept': departments_list}
    return render(request, 'department.html', context)


