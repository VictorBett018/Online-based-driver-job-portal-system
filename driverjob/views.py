from datetime import date
from lib2to3.pgen2 import driver
from this import d
from django.shortcuts import render,redirect
from matplotlib import image
from .models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request, 'index.html')
    

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"  
        except:
            error="yes" 
    d = {'error': error}             
    return render(request, 'admin_login.html', d)

def user_login(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = DriverUser.objects.get(user=user)
                if user1.type == "driver":
                    login(request,user)
                    error="no"
                else:   
                    error="yes" 
            except:
                error="yes"
        else:
          error="yes"
    d = {'error': error}
    return render(request, 'user_login.html', d)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')   
    return render(request, 'user_home.html')

def user_jobs(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    job = Job.objects.all().order_by('-start_date')
    user = request.user
    driver = DriverUser.objects.get(user=user)
    data = Apply.objects.filter(driver=driver)
    li=[]
    for i in data:
        li.append(i.job.id)
    d = {'job':job,'li':li}    
    return render(request, 'user_jobs.html',d)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    dcount = DriverUser.objects.all().count()
    ecount = Employer.objects.all().count()
    d = {'dcount':dcount,'ecount':ecount}
    return render(request, 'admin_home.html',d)    

def Logout(request):
    logout(request)
    return redirect('index')

def employer_login(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Employer.objects.get(user=user)
                if user1.type == "employer" and user1.status=="Accept":
                    login(request,user)
                    error="no"
                else:   
                    error="not" 
            except:
                error="yes"
        else:
          error="yes"
    d = {'error': error}
    return render(request, 'employer_login.html', d)

def employer_home(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    user =request.user
    employer = Employer.objects.get(user=user)
    job = Job.objects.filter(employer=employer)  
    d = {'job':job}      
    return render(request, 'employer_home.html',d)

def employer_profile(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    user = request.user   
    employer = Employer.objects.get(user=user)
    d = {'employer':employer}      
    return render(request, 'employer_profile.html',d)   

def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user   
    driver = DriverUser.objects.get(user=user)
    d = {'driver':driver}      
    return render(request, 'user_profile.html',d)   

def employer_register(request):
    error=""
    if request.method == 'POST':
      f = request.POST['fname']
      l = request.POST['lname']
      i = request.FILES['image']
      p = request.POST['pwd']
      e = request.POST['email']
      con = request.POST['contact']
      gen = request.POST['gender']
      com = request.POST['company']
      try:
        user = User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
        Employer.objects.create(user=user,mobile=con,image=i,gender=gen,company=com, type="employer" , status="pending")
        error= "no"

      except:
        error="yes"
    d = {'error' : error}
    return render(request, 'employer_register.html',d)

def user_register(request):
    error=""
    if request.method == 'POST':
      f = request.POST['fname']
      l = request.POST['lname']
      i = request.FILES['image']
      p = request.POST['pwd']
      e = request.POST['email']
      con = request.POST['contact']
      yol = request.POST['yearsoflicense']
      yoe = request.POST['yearsofexperience']
      loc = request.POST['location']
      gen = request.POST['gender']
      try:
        user = User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
        DriverUser.objects.create(user=user,mobile=con,image=i,gender=gen,yearsoflicense=yol,yearsofexperience = yoe,location= loc, type="driver")
        error= "no"

      except:
            error="yes"
    d = {'error' : error}
    return render(request, 'user_register.html',d)

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = DriverUser.objects.all()
    d = {'data':data}   
    return render(request, 'view_users.html',d)       

def del_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    driver = User.objects.get(id=pid)
    driver.delete()
    return redirect ('view_users') 

def employers(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Employer.objects.all()
    d = {'data':data}   
    return render(request,'employers.html',d) 

def employers_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Employer.objects.filter(status='pending')
    d = {'data':data}   
    return render(request, 'employers_pending.html',d)  

def employers_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Employer.objects.filter(status='Accept')
    d = {'data':data}   
    return render(request, 'employers_accepted.html',d)      

def employers_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Employer.objects.filter(status='Reject')
    d = {'data':data}   
    return render(request, 'employers_rejected.html',d)   

def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""    
    employer = Employer.objects.get(id=pid)
    if request.method=="POST":
        s = request.POST['status']
        employer.status=s
        try:
            employer.save()
            error="no"
        except:
            error="yes"

    d = {'employer':employer,'error':error}   
    return render(request, 'change_status.html',d)            
def del_employer(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employer = User.objects.get(id=pid)
    employer.delete()
    return redirect ('employers') 

def change_adminpwd(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""    
    if request.method=="POST":
        c = request.POST['cpass']
        n = request.POST['npass']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"    
        except:
            error="yes"

    d = {'error':error}   
    return render(request, 'change_adminpwd.html',d)      

def change_userpwd(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""    
    if request.method=="POST":
        c = request.POST['cpass']
        n = request.POST['npass']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"    
        except:
            error="yes"

    d = {'error':error}   
    return render(request, 'change_userpwd.html',d)  

def change_emppwd(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    error=""    
    if request.method=="POST":
        c = request.POST['cpass']
        n = request.POST['npass']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"    
        except:
            error="yes"

    d = {'error':error}   
    return render(request, 'change_emppwd.html',d) 

def post_job(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    error=""
    if request.method == 'POST':
      tit = request.POST['title']
      sd = request.POST['startdate']
      ed = request.POST['enddate']
      sal = request.POST['salary']
      car = request.FILES['car']
      exp = request.POST['experience']
      loc = request.POST['location']
      des = request.POST['description']
      user =request.user
      employer = Employer.objects.get(user=user)
      try:
        Job.objects.create(employer=employer,title=tit,start_date=sd,end_date=ed,salary=sal,image=car,experience=exp,location=loc,description=des,creationdate=date.today())
        
        error= "no"
      except:
        error="yes"
    d = {'error' : error}    
    return render(request, 'post_job.html',d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    user =request.user
    employer = Employer.objects.get(user=user)
    job = Job.objects.filter(employer=employer)  
    d = {'job':job}  
    return render(request, 'job_list.html',d) 

def edit_job(request,pid):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    error=""
    job = Job.objects.get(id=pid)
    if request.method == 'POST':
      sd = request.POST['startdate']
      ed = request.POST['enddate']
      sal = request.POST['salary']
      exp = request.POST['experience']
      des = request.POST['description']
    
     
      job.start_date=sd
      job.end_date=ed
      job.salary=sal
      job.experience=exp
      job.description=des

      try:
        job.save()
        error= "no"
      except:
        error="yes"
      if sd:
        try:
            job.start_date = sd
            job.save()
        except:
            pass
      else:
        pass
      if ed:
        try:
            job.end_date = ed
            job.save()
        except:
            pass
      else:
        pass

    d = {'error' : error,'job':job}    
    return render(request, 'edit_job.html',d)  

def del_job(request, pid):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    job = Job.objects.get(id=pid)
    job.delete()
    return redirect ('job_list')           

def all_jobs(request):
    data = Job.objects.all().order_by('-start_date')
    d = {'data':data}   
    return render(request, 'all_jobs.html',d) 

def job_details(request, pid):
    job = Job.objects.get(id  = pid)
    d = {'job':job}   
    return render(request, 'job_details.html',d) 

def apply_job(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    user =request.user
    driver = DriverUser.objects.get(user=user)
    job = Job.objects.get(id = pid)
    date1 =date.today()
    if job.end_date < date1:
        error="close"
    elif job.start_date > date1:
        error="notopen"
    else:
        if request.method == "POST":
            r = request.FILES['resume']
            Apply.objects.create(job=job,driver=driver,resume=r,applydate=date.today())
            error="done"
    d = {'error':error}   
    return render(request, 'apply_job.html',d)   

def applicants(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    data = Apply.objects.all()
    d = {'data':data}
    return render(request, 'applicants.html',d)

def drivers(request):
    if not request.user.is_authenticated:
        return redirect('employer_login')
    data = DriverUser.objects.all()
    d = {'data':data}   
    return render(request, 'drivers.html',d)  