from django.contrib import admin
from .models import Project, Story, Task


admin.site.register(Project)
admin.site.register(Story)
admin.site.register(Task)

