from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CourseTime, SavePriority, CreatePriority
from user.models import Profile
# Register your models here.
# UserAdmin.list_display += ('role',)
admin.site.register(Profile)
admin.site.site_header = 'Administration'
admin.site.register(CourseTime)
admin.site.register(SavePriority)
admin.site.register(CreatePriority)
