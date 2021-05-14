from django.contrib import admin

from .models import StudentInfo, DatabaseUser
# Register your models here.

admin.site.register(StudentInfo)
admin.site.register(DatabaseUser)
