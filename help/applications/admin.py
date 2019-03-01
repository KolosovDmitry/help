from django.contrib import admin
from .models import Applications, Company, Service, ServiceApplications, Kkt

# Register your models here.
class ApplicationsAdmin(admin.ModelAdmin):
	pass
	
class CompanyAdmin(admin.ModelAdmin):
	pass
													
#class CommentsAdmin(admin.ModelAdmin):
#	pass
															
class ServiceAdmin(admin.ModelAdmin):
	pass
	
class ServiceApplicationsAdmin(admin.ModelAdmin):
	pass
	
class KktAdmin(admin.ModelAdmin):
	pass
	
	
admin.site.register(Applications, ApplicationsAdmin)
admin.site.register(Kkt, KktAdmin)
admin.site.register(Company, CompanyAdmin)
#admin.site.register(Comments, CommentsAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceApplications, ServiceApplicationsAdmin)