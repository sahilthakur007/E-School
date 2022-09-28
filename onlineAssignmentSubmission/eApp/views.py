from multiprocessing import context
from urllib import request
from django.shortcuts import render,redirect
from .forms import TeacherProfileForm, TeacherRegistrationForm
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, "home.html")

def listAllSubjects(request):
    id = (int)(request.user.id)
    teacher = Teacher.objects.get(id=id+1)
    allsubjects = teacher.courses.all()
    print(id)
    context = {
        "subjects":allsubjects
    }
    return render(request,"list_all_subjects.html",context)


def listAllAssignmentForSubjects(request, course_id):
    course = Course.objects.get(id=course_id)
    allAssignments = course.assignment_set.all()
    
    context ={
        "assignments":allAssignments
    }
    return render(request, "list_all_assignments_for_subject.html", context)

def listAllSolutionForAssignment(request,assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    allSollutions = assignment.submission_set.all()
    print(allSollutions)
    context ={
        "sollutions": allSollutions
    }
    return render(request, "list_all_solutions_for_assignment.html", context)


def singleAssignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    print(assignment.question)
    context = {
        "assignment": assignment
    }
    return render(request, "singleAssignmentStudent.html", context)

def singleSolution(request, submission_id):
    solution = Submission.objects.get(id=submission_id)
    print(solution.answer)
    context = {
        "assignment": solution
    }
    return render(request, "Assignments/list_all_subjects.html", context)

def registerFaculty(request):
    form = TeacherRegistrationForm()
    if request.method=="POST":
        # print("true")
        form = TeacherRegistrationForm(request.POST)
        # tform = TeacherProfileForm(request.POST)
        
        if form.is_valid() :
            user = form.save()
            print("true")
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            user.set_password(user.password)
            user.save()
            # print(firstname+" "+lastname+" "+email+" "+password)
            Teacher.objects.create(firstname=firstname,lastname =lastname,email = email,password = password)
            return redirect("home")
        else:
            print(form.errors)
        
        
    context ={
        "form":form
    }
    return render(request,"signup.html",context)
def loginUser(request):
    # if request.user.is_authenticated:
        # return redirect("home")
    if request.method =="POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username+" "+password)
        
        user = authenticate(username= username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("allSubjects")
    return render(request,"login.html",{})
def logout(request):
    pass 

