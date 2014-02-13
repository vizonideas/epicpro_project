import json

from django.views.generic import ListView, DetailView, FormView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Team, Member
from .forms import RegisterUserTeamForm, TeamForm, MemberForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.http import HttpResponse


class AjaxMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class LoginView(TemplateView):
    template_name = 'projects/login.html'


class HomeRegisterView(FormView):
    form_class = RegisterUserTeamForm
    template_name = "projects/index.html"
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        user.username = "admin@%s" % form.cleaned_data['team'].replace(" ","").lower()
        user.email = form.cleaned_data['username']
        user.save()
        team = Team()
        team.boss = user
        team.name = form.cleaned_data['team']
        team.save()

        # todo > send email

        return super(HomeRegisterView, self).form_valid(form)


class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'projects/dashboard/dashboard.html'


class TeamHomeView(LoginRequiredMixin,TemplateView):
    template_name = 'projects/dashboard/team.html'


class ProjectsHomeView(LoginRequiredMixin,TemplateView):
    template_name = 'projects/dashboard/projects.html'


class ResumeHomeView(LoginRequiredMixin,TemplateView):
    template_name = 'projects/dashboard/resume.html'


class TeamUpdateView(LoginRequiredMixin,UpdateView):
    form_class = TeamForm
    model = Team
    success_url = reverse_lazy('team')
    template_name = 'projects/dashboard/team_teamform.html'

    def get_initial(self):
        return { 'pk': 1 }


class MemberListView(LoginRequiredMixin,ListView):
    context_object_name = 'members' # by default is object_list
    model = Member
    paginate_by = 10
    queryset = Member.objects.all()
    template_name = 'projects/dashboard/team_memberform.html'


class MemberCreateView(LoginRequiredMixin,CreateView):
    form_class = MemberForm
    model = Member
    success_url = reverse_lazy('team')
    template_name = 'projects/dashboard/team_memberform.html'


