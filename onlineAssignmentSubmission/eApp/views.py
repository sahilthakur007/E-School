from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request, "home.html")

def listAllSubjects(request,id):
    
    teacher = Teacher.objects.get(id=id)
    allsubjects = teacher.courses.all()
    context = {
        "subjects":allsubjects
    }
    return render(request,"Assignments/list_all_subjects.html",context)

