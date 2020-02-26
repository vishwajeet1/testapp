from django.db import models

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstName = models.CharField(max_length=100, blank=False)
    lastName = models.CharField(max_length=100, blank=False)
    mobile = models.CharField(max_length=100, blank=False,primary_key=True)
    email = models.CharField(max_length=100, blank=False)
    password=models.CharField(max_length=100, blank=False, default='abcx')
    
    class Meta:
        ordering = ['created']