import os

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from app.models import Document
from app.forms import DocumentForm

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/app")
    else:
        form = DocumentForm()
    return render(request, 'index.html', {
        'form': form,
        'documents': Document.objects.all(),
    })
