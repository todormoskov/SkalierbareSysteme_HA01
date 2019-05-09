from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import TODOForm
from .models import Aufgaben


def home(request):
    context = {
        'Aufgaben': Aufgaben.objects.all(),
    }
    return render(request, 'home/TODOTable.html', context)

def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TODOForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, f'neues TODO erstellt')
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TODOForm()
    return render(request, 'home/TODONew.html', {'form': form})

def edit(request, aufgabe_id):
    if request.method == 'POST':
        form = TODOForm(request.POST, instance=Aufgaben.objects.get(pk=aufgabe_id))
        if form.is_valid():
            form.save()
            messages.success(request, f'TODO bearbeitet')
            return HttpResponseRedirect('/')
    else:
        form = TODOForm(instance=Aufgaben.objects.get(pk=aufgabe_id))
    return render(request, 'home/TODOEdit.html', {'form': form})

def delete(request, aufgabe_id):
    if request.method == 'POST':
        form = TODOForm(request.POST, instance=Aufgaben.objects.get(pk=aufgabe_id))
        if form.is_valid():
            form.delete()
            messages.success(request, f'TODO gelöscht')
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/add')

def impressum(request):
    return render(request, 'home/Impressum.html')
