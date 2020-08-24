from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Employee
from .forms import addEmployee, addDepartment


# Create your views here.

# Function Base Views
# This function shows the all content to home.html
def home(request):
    employ = Employee.objects.all()
    return render(request, "employee/home.html", {'employee': employ})


# add forms = modelform_factory(Employee, exclude=[])   # shortcut to create ModelForm
# This function create form and add the employee to database
def add(request):
    if request.method == 'POST':
        form = addEmployee(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = addEmployee()
    return render(request, "employee/add.html", {"form": form})

# This function base view delete the data from database
def delete(request, id):
    if request.method == "POST":
        emp = Employee.objects.get(pk=id)
        emp.delete()
        return HttpResponseRedirect("/")

# This function base view update the details into database and retrieve old data from database
def update(request, id):
    if request.method == "POST":
        emp = Employee.objects.get(pk=id)
        form = addEmployee(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        emp = Employee.objects.get(pk=id)
        form = addEmployee(instance=emp)
    return render(request, "employee/update.html", {"form": form})

# This function create form and add the department to database
def add_dept(request):
    if request.method == 'POST':
        form = addDepartment(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = addDepartment()
    return render(request, "employee/dept.html", {"form": form})



# Class Base Views
# class EmployeeView(ListView):
#     model = Employee
#     context_object_name = "employee"
#     template_name = "employee/home.html"


# class AddView(CreateView):
#     model = Employee
#     template_name = "employee/add.html"
#     fields = ['Employee_Id', 'Name', 'Email', 'department']
#     success_url = reverse('home')
