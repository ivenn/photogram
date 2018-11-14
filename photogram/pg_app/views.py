from django.shortcuts import render

def index(request):
    context = {'res': "Hello world"}
    return render(request, 'pg_app/index.html', context)
