from django.shortcuts import render

def pantalla_inicial(request):
    """Docstring"""
    return render(request, 'index.html')
