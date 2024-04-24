from django.shortcuts import render
from django.http import HttpResponse

from .models import Index_work_page, Music, projectPage
from .forms import Contact_form

# Create your views here.
def index(request):
    dict_index_works ={
        'Index_work_page' : Index_work_page.objects.all(),
        'Music' : Music.objects.all()
    }

    return render(request, 'index.html', dict_index_works)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
    form = Contact_form()
    dict_form={
        'form': form
    }
    return render(request, 'contact.html', dict_form)





    
def project(request):
    dict_works ={
        'projectPage' : projectPage.objects.all(),
    }
    return render(request, 'projects.html', dict_works)

def projects(request,id):
    
    project = projectPage.objects.get(id = id)
    
    context ={
        'project': project
        
    }
    return render(request, 'projects_details.html', context)

