from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    idcard = models.CharField(max_length=20, primary_key=True)
    birthday = models.DateField(null=True)
    address = models.CharField(max_length=255, null=True)
    phonenumber = models.CharField(max_length=20,unique=True, default="xxxxxxxxxx")
    auth_user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True)

class Form(models.Model):
    name = models.CharField(max_length=100)
    auth_user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

class Input(models.Model):
    INPUT_TYPE =[
        ("short_answer","Short Answer"),
        ("multiple_choice","Multiple Choice"),
        ("numeric_answer","Numuric Answer"),
        ("dropdown","Dropdown"),
        ("date","Date"),
        ("idno","Id Card Number"),
        ("file","File")
    ]
    sequence = models.IntegerField()
    question = models.CharField(max_length=255)
    placehold = models.CharField(max_length=255)
    form = models.ForeignKey(Form, on_delete=models.SET_NULL,null=True)
    input_type = models.CharField(max_length=20, choices=INPUT_TYPE, default="")

class Option(models.Model):
    value = models.CharField(max_length=255)
    input_type = models.ForeignKey(Input,on_delete=models.SET_NULL,null=True)

class Respondent(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    value_string = models.CharField(max_length=255)
    value_integer = models.IntegerField()
    value_date = models.DateField()
    value_file = models.FileField()
    input_type = models.ForeignKey(Input,on_delete=models.SET_NULL,null=True)
    respondent = models.ForeignKey(Respondent,on_delete=models.SET_NULL,null=True)



    

