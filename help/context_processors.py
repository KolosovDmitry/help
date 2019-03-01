#from django.core.context_processors import request
 
#Импортируем модель категорий
from help.menu.models import Menu
from django.contrib.auth.models import User
from django.template.context_processors import request
 
def menu(request):
	group = request.user.groups.values_list('id', flat=True).first()
	menu_list = Menu.objects.filter(group__in=[group]).order_by('-title')
	return {'menu_list' : menu_list}