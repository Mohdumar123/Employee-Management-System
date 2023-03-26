from django.shortcuts import render, HttpResponse
from .models import Employee,Role,Department

def index(request):
    return render(request,'index.html')

def view_emp(request):
    emps = Employee.objects.all()
    context = {
      'emps' : emps
    }
    return render(request,'view_emp.html',context)

def add_emp(request):
    role = Role.objects.all()
    Dep = Department.objects.all()
    context = {
      'role' : role,
      'Dep' :Dep
    }
    if request.method == 'POST':
        f_n = request.POST['first_name']
        l_n = request.POST['last_name']
        sal = int(request.POST['salary'])
        bn = int(request.POST['bonus'])
        ph = int(request.POST['phone'])
        role = int(request.POST['role'])
        dept = int(request.POST['dept'])
        date = request.POST['hire_date']
        new_emp = Employee(first_name=f_n, last_name=l_n, salary=sal, bonus=bn, phone=ph, role_id=role, dept_id=dept, hire_date=date)
        new_emp.save()
        return HttpResponse("Employee added Successfully !!!")
    elif request.method == 'GET':
        return render(request,'add_emp.html',context)
    else:
        print("Something Went wrong")

def rm_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_rm = Employee.objects.get(id=emp_id)
            emp_to_be_rm.delete()
            return HttpResponse("Employee Remove Successfully !!!")
        except:
          return HttpResponse("Somethings went wrong")
        
    emp = Employee.objects.all()
    context = {
        "emps":emp
    }
    return render(request,'rm_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
      f_name = request.POST['first_name']
      l_name = request.POST['last_name']
      role = request.POST['role']
      dept = request.POST['dept']
      emp = Employee.objects.all()

      if f_name:
          emp = emp.filter(first_name__icontains = f_name)
      if l_name:
          emp = emp.filter(last_name__icontains = l_name)
      if dept:
          emp = emp.filter(dept__name__icontains = dept)
      if role:
          emp = emp.filter(role__name__icontains = role)
    
      context={
            "emps":emp
        }
      return render(request,'view_emp.html',context)
    
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    
    else:
        return HttpResponse("Something went wrong")
