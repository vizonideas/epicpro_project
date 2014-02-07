#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class AuditModel(models.Model):
    """
    An Abstract base class model that provides self-updating "create" , "delete" and "modified" fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False,editable=False)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


STATE_TASK_CHOICES = (
    ('todo', 'To Do'), # Pendientes
    ('inprogress', 'In Progress'), # En Desarrollo
    ('verify', 'Verify'), # Por Verificar
    ('done', 'Done'), # Terminadas
)


class Project(AuditModel):
    """Model Project"""
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User)

    class Meta:
        ordering = ('modified',)
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __unicode__(self):
        return u"%s" % (self.name,)


class Story(AuditModel):
    """Model Story"""
    project = models.ForeignKey(Project)
    description = models.TextField()
    order = models.IntegerField(default=1)

    class Meta:
        # db_table = 'music_album'
        ordering = ('order',)
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def __unicode__(self):
        return u"%s" % (self.description,)


class Task(AuditModel):
    """Model Task"""
    story = models.ForeignKey(Story)
    number = models.CharField(max_length=4)
    description = models.TextField()
    state = models.CharField(max_length=10, choices=STATE_TASK_CHOICES)
    owner = models.ForeignKey(User)

    class Meta:
        # db_table = 'music_album'
        ordering = ('number',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __unicode__(self):
        return u"%s" % (self.description,)