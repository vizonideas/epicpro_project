from django.core.urlresolvers import reverse

def menu(request):
	menu = {'menu': [
		{'name': 'Dashboard', 'url': reverse('dashboard')},
		{'name': 'Team', 'url': reverse('team')},
		{'name': 'Projects', 'url': reverse('projects')},
		{'name': 'Resume', 'url': reverse('resume')},
	]}
	for item in menu['menu']:
		if request.path == item['url']:
			item['active'] = True
	return menu