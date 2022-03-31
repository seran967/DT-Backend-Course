from app.internal.models.admin_user import AdminUser

from django.db import models

class City (models.Model):
	name = models.CharField(max_length=255)
	
class Place (models.Model):
	name = models.CharField(max_length=255)

class Person(models.Model):
	name = models.CharField(max_length=255)
	bio = models.TextField(blank=True)
	email = models.EmailField()
	date_of_birth = models.DateField()
	city = models.ForeignKey('app.City', on_delete=models.RESTRICT, related_name='people')
	favorite_places = models.ManyToManyField('app.Place')

def __str__(self):
	return f'{self.name}'

class Meta:
	verbose_name = 'Person'
	verbose_name_plural = 'People'
	


	
