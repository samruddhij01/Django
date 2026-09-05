from django.contrib import admin
from .models import student,emp,faculty,player,artist,deveploper,register

# Register your models here.
admin.site.register([student,emp,faculty,player,artist,deveploper,register])
