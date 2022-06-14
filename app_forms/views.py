from http.client import REQUEST_ENTITY_TOO_LARGE
import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserInfo
from .models import Form
from .models import Input
from .models import Option
from .models import Respondent
from .models import Answer
import datetime
from app_forms.forms import AppForm
import json
from django.http import QueryDict
from querystring_parser import parser


# Create your views here.

def index(request):
    
    return render(request,"index.html")

def register(request):
    return render(request,"register.html")

def checkRegister(request):
    username = request.POST["username"]
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    # birthday = request.POST["birthday"]
    # # idcard = request.POST["idcard"]
    # address = request.POST["address"]
    email = request.POST["email"]
    # phonenumber = request.POST["phonenumber"]
    password1 = request.POST["password1"]
    password2 = request.POST["password2"]

    if password1==password2:
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username นี้มีแล้ว")
            return redirect ("/register")
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email นี้มีแล้ว")
            return redirect ("/register")
        # elif User.objects.filter(idcard=idcard).exists():
        #     messages.info(request,"ID CARD นี้มีแล้ว")
            return redirect ("/register")
        # elif User.objects.filter(phonenumber=phonenumber).exists():
            messages.info(request,"เบอร์โทรนี้มีแล้ว")
            return redirect ("/register")

        else:
            user = User.objects.create_user(
            
            username=username,
            password=password1,
            first_name=firstname,
            last_name=lastname,
            email=email
            # birthday=birthday,
            # email=email,
            # address=address,
            # phonenumber=phonenumber
            )
            user.save()
            return redirect("/")
    else:
        messages.info(request,"รหัสผ่านไม่เหมือนกัน")
        return redirect ("/register")


def login(request):
    return render(request,"login.html")

def checkLogin(request):
    username = request.POST["username"]
    password = request.POST["password"]

    # login check username password ว่าถูกต้องไหม
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return redirect("/")
    else:
        messages.info(request,"หาข้อมูลไม่พบ")
        return redirect("/login")

def logout(request):
    auth.logout(request)
    return redirect("/")
# def dashboard(request):
#     return render(request,"dashboard.html")

# def draft(request):
#     return render(request,"draft.html")

def createForm(request):
    return render(request,"createForm.html")

def addInput(request):
    form = AppForm()
    context = {
        "form": form
    }
    return render(request,"/partials/form.html",context)

def userForm(request):
    oUser = request.user
    userid = oUser.id
    today = datetime.date.today()
    birthday = today
    idno = "xx"
    address = "xx"
    phonenumber = "xx"

    if UserInfo.objects.filter(auth_user_id=userid).exists():
        userinfo = UserInfo.objects.get(auth_user_id=userid)
        birthday = userinfo.birthday
        idno = userinfo.idcard
        address = userinfo.address
        phonenumber = userinfo.phonenumber

    return render(request,"user.html",{"birthday":birthday,"idno":idno,"address":address,"phonenumber":phonenumber})


def userUpdate(request):
    oUser = request.user
    userid = oUser.id
    username = request.POST["username"]
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    email = request.POST["email"]
    birthday = request.POST["birthday"]
    idno = request.POST["idcard"]
    address = request.POST["address"]
    phonenumber = request.POST["phonenumber"]

    # user = User()
    # user.username = username
    # user.first_name=firstname
    # user.last_name=lastname
    # user.email=email
    # user.save()

    userinfo = UserInfo()
    userinfo.idcard = idno
    userinfo.birthday = birthday
    userinfo.address = address
    userinfo.phonenumber = phonenumber
    userinfo.auth_user_id = userid
    userinfo.save()
    messages.info(request,"แก้ไขข้อมูลเรียบร้อย")
    return redirect("/")

def saveForm(request):
    if request.method == "POST":
        oUser = request.user
        userid = oUser.id
        oForm = Form()
        oForm.name = "default"
        oForm.auth_user_id = userid
        oForm.save()
        print(oForm.id)
        
        post_dict = parser.parse(request.POST.urlencode())
        no = 0
        a = post_dict["input"]
        for i in a: 
            oInput = Input()
            oInput.input_type = a[i]["type"]
            oInput.question = a[i]["question"]
            oInput.placehold = a[i]["holder"]
            oInput.sequence = no
            no= no+1
            oInput.form_id = oForm.id
            print("--------------------------------------")
            print(no)
            oInput.save()

        messages.info(request,"สร้างฟอร์มเรียบร้อย")  

    return redirect("/")