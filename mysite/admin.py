from django.contrib import admin
from .models import MyResume

class MyResumeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'image',
                    'email', 'phone_number', 'address', 'education',
                    'experience', 'skills', 'languages', 'certifications', 'hobbies')

admin.site.register(MyResume, MyResumeAdmin)
