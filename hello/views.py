from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_view(request):
    return render(request, 'home.html', {'title': 'home'})

def about(request):
    context = {
        'title': 'about',
        'name': 'Glaiza',
        'student_id': '202410123',
    }
    return render(request, 'about.html', context)