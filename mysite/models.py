from django.db import models


class MyResume(models.Model):
        first_name = models.CharField(max_length=25)
        last_name = models.CharField(max_length=25)
        image = models.CharField(max_length=250, null=True)
        email = models.EmailField()
        phone_number = models.CharField(max_length=15)
        address = models.TextField()
        summary = models.TextField()
        education = models.TextField()
        experience = models.TextField()
        skills = models.TextField()
        # languages = models.TextField()
        certifications = models.TextField()
        hobbies = models.TextField()
