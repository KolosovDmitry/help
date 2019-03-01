#from django.core.context_processors import request
 
#Импортируем модель категорий
from .models import Menu
 
def menu(request):
	menu_list = Menu.objects.all()    
	return {"menu_list":menu_list}