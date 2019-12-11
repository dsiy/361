from django.contrib import admin
from .models import CourseTime, SavePriority, CreatePriority

# Register your models here.
admin.site.register(CourseTime)
admin.site.register(SavePriority)
admin.site.register(CreatePriority)
