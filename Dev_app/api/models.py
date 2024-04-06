from django.db import models
from django.dispatch import receiver
from django.utils import timezone
# from django.db.models.signals import post_save

class UpcomingEvent(models.Model):
    title = models.CharField(max_length = 150)
    description = models.TextField()
    imageUrl = models.ImageField(upload_to='pendingTask')
    isCompleted = models.BooleanField(default = False)
    date_posted = models.DateField(auto_now_add = True)

    # @receiver(post_save,sender=UpcomingEvent)
    # def updated_date(sender,instance,created,**kwargs):
    #     if instance.isCompleted:
    #         instance.data_completed = timezone.now()
    #         instance.save()



    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    date_posted = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title

class Email(models.Model):
    email = models.EmailField(max_length= 50)
    contact = models.CharField(max_length = 10)

    def __str__(self):
        return self.email
    
class UserDetailTesting(models.Model):
    username = models.CharField(max_length = 40)
    activEmail = models.ForeignKey(Email,on_delete = models.CASCADE,related_name = 'usedetail')

    def __str__(self):
        return self.username