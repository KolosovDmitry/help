# coding=utf-8
from django import forms
from .models import Applications, Service, Company, Comments
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class ApplicationsCreateForm(forms.ModelForm):
	#service = forms.ModelMultipleChoiceField(label='Выбор услуг',widget=forms.CheckboxSelectMultiple, queryset=Service.objects.all())
	#company = forms.ModelChoiceField(label='Выбор компании',queryset=Company.objects.all())
	class Meta:
		model = Applications
		fields = ['company','bill','files','namber','type_of_service','service','product']
		
		labels = {'namber':'Колличество ККТ','bill':'Счёт','files':'Файл','company':'Компания','type_of_service':'Где ','service':'Услуги ','product':'Продукт '}
		
	def __init__(self, *args, **kwargs):
		super(ApplicationsCreateForm, self).__init__(*args, **kwargs)
		self.fields['company'].widget.attrs.update({'id':'mySelect'})
		self.fields['product'].widget.attrs.update({'id':'mySelectNo', 'class':'form-control-sm'})
		self.fields['type_of_service'].widget.attrs.update({'id':'mySelectNo'})
		self.fields['service'].widget.attrs.update({'id':'mySelectMulti'})
		self.fields['bill'].widget.attrs.update({'class':'form-control-sm'})
		self.fields['namber'].widget.attrs.update({'class':'form-control-sm'})
		
		
class CompanyCreateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
	class Meta:
		model = Company
		fields = ['inn','name']
		labels = {'inn':'ИНН-КПП','name':'Наименование компании'}
		
class CommentsForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ['content']
	def __init__(self, *args, **kwargs):
		super(CommentsForm, self).__init__(*args, **kwargs)
		self.fields['content'].widget.attrs.update({'class':'form-control', 'rows':'3'})
		
		
		
		