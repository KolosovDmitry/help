from django.shortcuts import render, HttpResponseRedirect, get_object_or_404,redirect, render_to_response
from .models import Applications, Comments, Company, ServiceApplications, Service
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, DetailView, CreateView, ListView
from django.views import View
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import ApplicationsCreateForm, CompanyCreateForm, CommentsForm
from bootstrap_modal_forms.mixins import PassRequestMixin
from django.views.generic.edit import FormMixin
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def login(requests):
	clientId = "i2ts_app"
	clientSecret = "z91zQPmSzWXSkI6G4k0P"
	url = 'https://passport.skbkontur.ru/v3/connect/token'
	payload = {"grant_type": "client_credentials", "scope": "profiles"}
	r = Request('POST',url, params=payload)
	
class ApplicationsListView(LoginRequiredMixin,ListView):
	
	context_object_name = 'applications'
	template_name = 'applications/index.html'
	def get(self, request, *args, **kwargs):
		context = {}
		if request.user.is_staff:
			applications_list = Applications.objects.all()
		else:
			applications_list = Applications.objects.filter(creator=request.user).filter(responsible=request.user)
		current_page = Paginator(applications_list, 10)
		page = request.GET.get('page')
		try:
			context['applications_list'] = current_page.page(page)
			
			
		except PageNotAnInteger:
			context['applications_list'] = current_page.page(1)
			
		except EmptyPage:
			context['applications_list'] = current_page.page(current_page.num_pages)
		return render_to_response(template_name=self.template_name, context=context)
		
class ApplicationsDetailView(LoginRequiredMixin,DetailView,FormMixin):
	model = Applications
	template_name = 'applications/applications_detail.html'
	form_class = CommentsForm
	
	#applications = get_object_or_404(Applications, id=id)
	#comment = Comments.objects.filter(applications = applications).order_by('pub_date')
	
	def get_context_data(self, **kwargs):
		context = super(ApplicationsDetailView, self).get_context_data(**kwargs)
		comment_list = (
            Comments.objects.filter(applications=self.object).order_by('pub_date')
        )
		context['comment_tree'] = comment_list
		context['comment_form'] = self.form_class(initial={
            'applications_id': self.object
        })
		return context
		
	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		form.author = request.user
		#form.applications_id = self.objects
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		
		form.save()
		return super(ApplicationsDetailView, self).form_valid(form)



class ApplicationsCreateView(LoginRequiredMixin,CreateView):
	model = Applications
	template_name = 'applications/applications_create.html'
	form_class = ApplicationsCreateForm
	#fields = ['namber','bill','files','date_of_service','company','type_of_service','service','product']
	labels = {'namber':'Колличество ККТ','bill':'Счёт','files':'Файл','date_of_service':'Дата оказания услуги','company':'Компания','type_of_service':' ','service':' ','product':' '}
	
	def form_valid(self, form):
		form.instance.creator = self.request.user
		form.save()
		return redirect("/applications/all_applications/")
     
	def success_url(self):
		return redirect("/applications/all_applications/")
	
class ApplicationsUpdateView(LoginRequiredMixin,UpdateView):
	model = Applications
	fields = ['creator','date_of_service','company','type_of_service','service','product']
	template_name_suffix = '_update_form'
											
		
class ApplicationsMyListView(LoginRequiredMixin,ListView):
	
	context_object_name = 'applications'
	template_name = 'applications/my_applications.html'
	#@method_decorator(login_required)
	def get(self, request, *args, **kwargs):
		context = {}
		if request.user.is_staff:
			applications_list = Applications.objects.filter(Q(creator=request.user) | Q(responsible=request.user))
		
		current_page = Paginator(applications_list, 5)
		page = request.GET.get('page')
		try:
			context['applications_list'] = current_page.page(page)
			
			
		except PageNotAnInteger:
			context['applications_list'] = current_page.page(1)
			
		except EmptyPage:
			context['applications_list'] = current_page.page(current_page.num_pages)
		return render_to_response(template_name=self.template_name, context=context)
		
class CompanyCreateView(LoginRequiredMixin,PassRequestMixin,CreateView):
	model = Company
	template_name = 'company/company_create.html'
	form_class = CompanyCreateForm
	success_message = 'Компания добавлена'
	#success_url = reverse_lazy('ApplicationsCreate')
	
	
class CompanyDetailView(LoginRequiredMixin,DetailView):
	model = Company
	template_name = 'company/company_detail.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		return context
		
class CompanyListView(LoginRequiredMixin,ListView):
	
	context_object_name = 'company'
	template_name = 'company/index.html'
	def get(self, request, *args, **kwargs):
		context = {}
		if request.user.is_staff:
			company_list = Company.objects.all()
			applications_list = Applications.objects.all()
		
		current_page = Paginator(company_list, 10)
		page = request.GET.get('page')
		try:
			context['company_list'] = current_page.page(page)
			
			
		except PageNotAnInteger:
			context['company_list'] = current_page.page(1)
			
		except EmptyPage:
			context['company_list'] = current_page.page(current_page.num_pages)
		return render_to_response(template_name=self.template_name, context=context)
	