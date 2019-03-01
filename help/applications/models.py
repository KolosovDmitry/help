from django.db import models
from django.conf import settings
from datetime import date
from django.template.context_processors import request

class Service(models.Model):#Модель услуг
	name = models.CharField('Название услуги',max_length=100000)
	price = models.DecimalField('Цена',max_digits=6, decimal_places=2)
	description = models.TextField('Описание')
	    
	def __str__(self): 
		return (self.name)
	def get_absolute_url(self):
		return "/price/%i/" % self.id
			    
class Company(models.Model):#Модель организациё
	name = models.CharField(max_length=100)
	inn = models.CharField(max_length=100)

	def __str__(self): 
		return (self.name)
		
	def get_absolute_url(self):
		return "/company/%i/" % self.id
						    
class Kkt(models.Model):
	name = models.CharField(max_length=100,null=True,blank=True)						    
						     
def user_directory_path(self, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
	return "file/application_{id}/user_{userid}/{filename}".format(userid = self.creator.id, id = self.id, filename = filename)						     
					     
class Applications(models.Model):
	SERVICE = 'SV' #Сервис и настройки
	#MARKET = 'MK' #Маркет
	#KEP = 'KP' #КЭП
	#NO = 'NO' #Неназначено
	NEW = 'NW' #Новый
	CLOSE = 'CS' #Закрыт
	REFUSAL = 'RL' #Отказ
	#APPOINTED = 'AD' #Назначен
	IN_WORK = 'IW' #В работе
	OFFICE = 'OF' #Работа в офисе
	REMOTE = 'RM' #Удаленная работа
	TRIP = 'TP' #Выездная работа
	TYPE_CHOICES = ((OFFICE,'Работа в офисе'),(REMOTE,'Удаленная работа'),(TRIP,'Выездная работа'))
	PRODUCT_CHOICES = ((SERVICE, 'Сервис и настройки'),)
	STATUS_CHOICES = ((NEW,'Новый'),(CLOSE,'Закрыт'),(REFUSAL,'Отказ'),(IN_WORK,'В работе'))
			    							    
	creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='creator') #Кто создал работу
	creation_date = models.DateTimeField(auto_now_add=True) #Дата создания работы
	date_of_service = models.DateField(null=True, blank=True) #Дата исполнения
	date_of_change = models.DateTimeField(auto_now=True) #Дата изменения работы
	company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='company') #Компания
	type_of_service = models.CharField(max_length=2,choices=TYPE_CHOICES,default=OFFICE) #3 варианта выбора(офис, удаленно, выезд)
	service = models.ManyToManyField(Service) #Услуги
	product = models.CharField(max_length=2,choices=PRODUCT_CHOICES,default=SERVICE)#Продукт(маркет, кэп ...)
	incident = models.CharField(max_length=100,null=True, blank=True) #Номер инцидента
	responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='responsible', null=True, blank=True) #Кто ответственный за работу, назначается руковадителем отдела
	#comments = models.ManyToManyField(Сomments) #Комментарии к работе
	files = models.FileField(upload_to=user_directory_path,null=True, blank=True) #Поле для загрузки файла.
	status = models.CharField(max_length=2,choices=STATUS_CHOICES,default=NEW) #Статус работы
	bill = models.CharField(max_length=100) #Номера счетов услуг
	kkt = models.ManyToManyField(Kkt)
	kkt_sn  = models.CharField(max_length=100,null=True,blank=True)
	namber = models.IntegerField()
	
	
	
	
	def get_absolute_url(self):
		return "/applications/%i/" % self.id
		
	def __str__(self): 
		return (self.company.name)
		
	
						    																	
						    																	    
class ServiceApplications(models.Model):
	
	applications = models.ForeignKey(Applications, on_delete=models.CASCADE)
	name = models.ManyToManyField(Service)
	#price = models.DecimalField(max_digits=6, decimal_places=2)
	
						    																		    
class Comments(models.Model):
	applications = models.ForeignKey(Applications,on_delete=models.CASCADE) 
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) 
	content = models.TextField('Комментарий')
	pub_date = models.DateTimeField('Дата комментария', auto_now_add=True)