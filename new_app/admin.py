from django.contrib import admin
from new_app.models import Task, User_model

# Register your models here.

admin.site.register(Task)

admin.site.register(User_model)