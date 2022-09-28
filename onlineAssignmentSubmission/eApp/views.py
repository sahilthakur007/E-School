from multiprocessing import context
from urllib import request
from django.shortcuts import render,redirect
from .forms import TeacherProfileForm
from .models import *
from django.contrib.auth import authenticate,login,logout
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


def listAllAssignmentForSubjects(request, course_id):
    course = Course.objects.get(id=course_id)
    allAssignments = course.assignment_set.all()
    
    context ={
        "assignments":allAssignments
    }
    return render(request, "Assignments/list_all_subjects.html", context)

def listAllSolutionForAssignment(request,assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    allSollutions = assignment.submission_set.all()
    print(allSollutions)
    context ={
        "sollutions": allSollutions
    }
    return render(request, "Assignments/list_all_subjects.html", context)


def singleAssignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    print(assignment.question)
    context = {
        "assignment": assignment
    }
    return render(request, "Assignments/list_all_subjects.html", context)


def singleSolution(request, submission_id):
    solution = Submission.objects.get(id=submission_id)
    print(solution.answer)
    context = {
        "assignment": solution
    }
    return render(request, "Assignments/list_all_subjects.html", context)


def registerFaculty(request):
    
    if request.method=="POST":
        print("true")
        form = TeacherProfileForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TeacherProfileForm()
    context ={
        "form":form
    }
    return render(request,"Assignments/register.html",context)
def loginUser(request):
    # if request.user.is_authenticated:
        # return redirect("home")
    if request.method =="POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username+" "+password)
        user = authenticate(request,Email = username,Password = password)
        print(user)
    return render(request,"Assignments/login.html",{})
def logout(request):
    pass 

