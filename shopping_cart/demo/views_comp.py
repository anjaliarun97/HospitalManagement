from django.shortcuts import render, redirect

from .forms import contactForm
from .models import Contacts


# Create your views here.
def createContact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact')
    else:
        form = contactForm()
    return render(request, 'contactcreate.html', {'form': form})


def listContact(request):
    lists = Contacts.objects.all().order_by('name')
    print('list', lists)
    return render(request, 'contactList.html', {'lists': lists})


def updateContact(request, list_id):
    update_contact = Contacts.objects.get(id=list_id)
    if request.method == 'POST':
        form = contactForm(request.POST, instance=update_contact)
        if form.is_valid():
            form.save()
            return redirect('/contact')
    else:
        form = contactForm(instance=update_contact)
    return render(request, 'contactUpdate.html', {'form': form})


def deleteContact(request, list_id):
    lists = Contacts.objects.get(id=list_id)
    if request.method == "POST":
        lists.delete()
        return redirect('/contact')
    return render(request, 'delete.html', {'lists': lists})
