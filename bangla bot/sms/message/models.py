from django.db import models
from django.contrib.auth.models import User




class Contact(models.Model): #delete
    		
	usr=models.ForeignKey(User,blank=True,
        null=True, on_delete = models.CASCADE)
	question=models.CharField(max_length=255 ,blank=True)

	answer = models.TextField(blank=True)
	
	def __str__(self):
		return self.question


class qnat(models.Model):
    		
	usr=models.ForeignKey(User,blank=True,
        null=True, on_delete = models.CASCADE)
	question=models.TextField(blank=True)

	answer = models.TextField(blank=True)
	
	def __str__(self):
		return self.question

'''
class Contact(models.Model):
    		
	usr=models.ForeignKey(User,blank=True,
        null=True, on_delete = models.CASCADE)
	name=models.CharField(max_length=255)
	number = models.IntegerField()
	info = models.TextField()
	
	def __str__(self):
		return self.name



class Message(models.Model):
    
	campaign_name=models.CharField(max_length=255)
	user_id=models.CharField(max_length=130)
	#contact = models.ForeignKey('Contact', on_delete = models.DO_NOTHING)
	contact = models.IntegerField()
	
	
	enter_message = models.TextField()
	


	def __str__(self):
		return self.campaign_name


class Message(models.Model):
    
	campaign_name=models.CharField(max_length=255)
	user_id=models.CharField(max_length=130)
	usr=models.ForeignKey(User,blank=True,
        null=True, on_delete = models.CASCADE)

	#contact = models.ForeignKey('Contact', on_delete = models.DO_NOTHING)
	contact = models.OneToOneField('Contact',on_delete=models.CASCADE)
	
	
	enter_message = models.TextField()
	


	def __str__(self):
		return self.campaign_name





class GroupMessage(models.Model):
    
	campaign_name=models.CharField(max_length=255)
	user_id=models.CharField(max_length=130)
	usr=models.ForeignKey(User,blank=True,
        null=True, on_delete = models.CASCADE)
	
	contact_num = models.ManyToManyField('Contact')
	
	enter_message = models.TextField()
	


	def __str__(self):
		return self.campaign_name





class Post(models.Model):
    
	sno=models.AutoField(primary_key=True)
	title=models.CharField(max_length=255)
	content=models.TextField()
	author = models.CharField(max_length=13)
	slug = models.CharField(max_length=130)
	


	def __str__(self):
		return self.title + ' by ' + self.author


'''