from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

#모델이 디비이고 동작이 있다. 
#디비를 어떻게 수정 할 지 정의된 동작들.

class Shop(models.Model):
	name = models.CharField(max_length=200)
	create_date = models.DateTimeField(default=timezone.now)
	update_date = models.DateTimeField(blank=True, null=True)	
	status = models.CharField(max_length=10)
	description = models.CharField(max_length=300)
	#가게가 오픈하는 행위 
	def open(self):
		self.create_date = timezone.now()
		self.save()
	#가게가 문을 닫는 행위 
	def close(self):
		self.update_date = timezone.now()
		self.save()		
	# 가게가 이벤트를 여는 행위?	
	def __str__(self):
		return self.name