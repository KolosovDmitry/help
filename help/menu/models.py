from django.db import models

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group

from django.dispatch import receiver

class Menu(models.Model):
	class Meta:
		verbose_name = 'Пункт меню'
		verbose_name_plural = 'Пункты меню'
		permissions = (
            ('menu_view', 'can view menu'),
            
        )
	
	slug = models.SlugField()
	active = models.BooleanField(verbose_name='Активность', default=True)
	title = models.CharField(verbose_name='Название  меню', max_length=50)
	url = models.CharField(max_length=100, help_text='Ссылка, например /about/ или http://foo.com/')
	group = models.ManyToManyField(Group, verbose_name = 'Группа доступа')
	def __str__(self):
		return self.title
