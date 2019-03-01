from django.contrib import admin
from .models import Menu

from django.db import models
# Register your models here.
#class MenuAdmin(admin.ModelAdmin):
#	group = forms.MultipleChoiceField(choices=SAMPLE_CHOICES, widget=forms.CheckboxSelectMultiple)
	


class MenuAdmin(admin.ModelAdmin):
    pass



admin.site.register(Menu, MenuAdmin)

