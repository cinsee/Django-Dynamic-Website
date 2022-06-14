import imp
from django.contrib import admin
from .models import UserInfo
from .models import Form
from .models import Input
from .models import Option
from .models import Respondent
from .models import Answer
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Form)
admin.site.register(Input)
admin.site.register(Option)
admin.site.register(Respondent)
admin.site.register(Answer)