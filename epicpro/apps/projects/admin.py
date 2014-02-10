from django.contrib import admin
from .models import Project, Story, Task, Team, Comment, Material


admin.site.register(Project)
admin.site.register(Story)
admin.site.register(Task)
admin.site.register(Team)
admin.site.register(Comment)
admin.site.register(Material)

