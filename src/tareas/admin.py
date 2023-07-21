from django.contrib import admin
from .models import Tarea
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


admin.site.register(Tarea)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    list_filter = ('is_staff', 'is_superuser')


#admin.site.register(UserAdmin)