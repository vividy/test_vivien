import os

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from app.models import Document
from app.forms import DocumentForm

def index(request):
    if request.method == 'POST' and request.user:
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = DocumentForm()
    return render(request, 'index.html', {
        'form': form,
        'documents': Document.objects.all().order_by('-uploaded_at')[:20],
    })


def login(request):
    return render(request, 'login.html')
