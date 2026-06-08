from django.shortcuts import render

# Create your views here.

def index(request):
    """La página de inicio para Learning Log"""
    return render(request, 'learning_logs/index.html')