import json

from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse_lazy

from .models import Team
from .forms import RegisterUserTeamForm

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


class HomeRegisterView(LoginRequiredMixin,FormView):
    form_class = RegisterUserTeamForm
    template_name = "projects/index.html"
    success_url = reverse_lazy('login_view')

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
    template_name = 'projects/dashboard.html'