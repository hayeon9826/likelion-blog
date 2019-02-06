from django.shortcuts import render, redirect, get_object_or_404
import os
from django.http import HttpResponse
from django.conf import settings
from .models import Portfolio
from .forms import PortfolioForm
from django.utils import timezone

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

def new_portfolio(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.published_at = timezone.now()
            portfolio.save()
            return redirect('portfolio')
    else:
        form = PortfolioForm()
    return render(request, 'portfolio/new.html', {'form':form})

def portfolio_detail(request, portfolio_id):
        post = get_object_or_404(Portfolio, pk=portfolio_id)
        return render(request, 'portfolio/detail.html', {'portfolio' :post})

def portfolio_remove(request, pk):
        portfolio = get_object_or_404(Portfolio, pk=pk)
        portfolio.delete()
        return redirect ('portfolio')
