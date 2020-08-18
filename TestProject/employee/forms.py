from django.forms import ModelForm
from .models import Employee, Department


class addEmployee(ModelForm):
    class Meta:
        model = Employee
        fields = ['Employee_Id', 'Name', 'Email', 'department']


class addDepartment(ModelForm):
    class Meta:
        model = Department
        fields = ['department', 'department_id']
