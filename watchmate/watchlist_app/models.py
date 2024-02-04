from django.db import models

# Create your models here.

class StreamPlateform(models.Model):
    name = models.CharField(max_length = 30)
    about = models.TextField(max_length = 45)
    website = models.URLField()
    
    def __str__(self):
        return self.name

class Watchlist(models.Model):
	title = models.CharField(max_length = 30)
	description = models.TextField(max_length=200)
	plateform = models.ForeignKey(StreamPlateform,on_delete = models.CASCADE,related_name = 'watchlist')
	active = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add = True)


	def __str__(self):
		return self.title	