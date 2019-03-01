from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt
#from help.applications.views import ApplicationsListView
app_name = 'help.applications'

urlpatterns = [
	path('all_applications/', views.ApplicationsListView.as_view(), name = 'ApplicationsList'),
	path('<int:pk>/',views.ApplicationsDetailView.as_view(), name = 'ApplicationsDetail'),
	path('<int:pk>/update/',views.ApplicationsUpdateView.as_view(), name = 'ApplicationsUpdate'),
	path('create/',views.ApplicationsCreateView.as_view(), name = 'ApplicationsCreate'),
	path('company_create/',views.CompanyCreateView.as_view(), name = 'CompanyCreate'),
	path('company/<int:pk>/',views.CompanyDetailView.as_view(), name = 'CompanyDetail'),
	path('my_applications/', views.ApplicationsMyListView.as_view(), name = 'ApplicationsMyList'),
	path('login/', csrf_exempt(views.login), name = 'login'),
	
	
]


