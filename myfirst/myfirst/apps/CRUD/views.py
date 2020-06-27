from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CRUD
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CRUDForm
from django.views.generic import ListView, DetailView

# Create your views here.





class Index(ListView):
    template_name = 'CRUD/index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return CRUD.objects.all()


class ContactDetailView(DetailView):
    model = CRUD
    template_name = 'CRUD/CRUD-detail.html'


def create(request):
    if request.method == 'POST':
        form = CRUDForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/CRUD/")
    form = CRUDForm()

    return render(request, 'CRUD/create.html', {'form': form})


def edit(request, pk, template_name='CRUD/edit.html'):
    contact = get_object_or_404(CRUD, pk=pk)
    form = CRUDForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/CRUD/")
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='CRUD/confirm_delete.html'):
    contact = get_object_or_404(CRUD, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return HttpResponseRedirect("/CRUD/")
    return render(request, template_name, {'object': contact})
