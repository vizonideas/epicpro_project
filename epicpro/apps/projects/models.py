#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class AuditModel(models.Model):
    """
    An Abstract base class model that provides self-updating "create" , "delete" and "modified" fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False,editable=False)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


STATE_MEMBER_CHOICES = (
    ('A', 'Active'),
    ('I', 'Innactive'),
)


STATE_TASK_CHOICES = (
    ('todo', 'To Do'), # Pendientes
    ('inprogress', 'In Progress'), # En Desarrollo
    ('verify', 'Verify'), # Por Verificar
    ('done', 'Done'), # Terminadas
)


UNIT_TASK_CHOICES = (
    ('h', 'hour(s)'),
    #('d', 'day(s)'),
)


class Team(AuditModel):
    """Model Team"""
    boss = models.ForeignKey(User, related_name='boss')
    members = models.ManyToManyField(User, through='Member')
    name = models.CharField(max_length=100)
    slut = models.CharField(max_length=100)
    resumen = models.CharField(max_length=100, blank=True, null=True)
    max_users = models.IntegerField(default=6)
    work_hour = models.IntegerField(default=8)

    def get_absolute_url(self):
        return reverse("team", kwargs={"pk": self.pk})

    class Meta:
        ordering = ('modified',)
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __unicode__(self):
        return u"%s" % (self.name,)


class Member(AuditModel):
    team = models.ForeignKey(Team)
    user = models.ForeignKey(User)
    state = models.CharField(max_length=10, choices=STATE_MEMBER_CHOICES)
    can_create_project = models.BooleanField(default=False)

    class Meta:
        ordering = ('modified',)
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __unicode__(self):
        return u"%s" % (self.state,)


class Project(AuditModel):
    """Model Project"""
    owner = models.ForeignKey(User, related_name='owner')
    team = models.ForeignKey(Team, blank=True, null=True)
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    resumen = models.CharField(max_length=100, blank=True, null=True)

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
    owner = models.ForeignKey(User)
    number = models.CharField(max_length=4)
    duration = models.IntegerField(default=0)
    real_duration = models.IntegerField(default=0)
    unit = models.CharField(max_length=1,default='h', choices=UNIT_TASK_CHOICES)
    description = models.TextField()
    state = models.CharField(max_length=10, choices=STATE_TASK_CHOICES)

    class Meta:
        # db_table = 'music_album'
        ordering = ('number',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __unicode__(self):
        return u"%s" % (self.description,)


class Comment(AuditModel):
    """Model Comment"""
    task = models.ForeignKey(Task)
    user = models.ForeignKey(User)
    text = models.TextField(blank=True, null=True)

    class Meta:
        # db_table = 'music_album'
        ordering = ('created',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __unicode__(self):
        return u"%s" % (self.text,)


class Material(AuditModel):
    """Model Task"""
    task = models.ForeignKey(Task)
    user = models.ForeignKey(User)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='material')

    class Meta:
        # db_table = 'music_album'
        ordering = ('created',)
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'

    def __unicode__(self):
        return u"%s" % (self.file,)