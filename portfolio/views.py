from django.shortcuts import render
import os
from django.http import HttpResponse
from django.conf import settings
from .models import Portfolio

# Create your views here.

def portfolio(request):
    posts = Portfolio.objects.all().order_by('-id')
    return render(request, 'portfolio/portfolio.html', {'post' : posts})

def pdf_download(request):
    filepath = os.path.join(settings.BASE_DIR,  'likelion2018.pdf')
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = 'application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response