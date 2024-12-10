from django.contrib import admin
from app11.models import logintable
from app11.models import usertable
from app11.models import  personaltable


# Register your models here.
admin.site.register(logintable)
admin.site.register(usertable)
admin.site.register(personaltable)


