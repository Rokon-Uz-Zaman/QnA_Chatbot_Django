from django.db import models

# Create your models here.

#author roman

class Qna(models.Model):
	question=models.TextField(blank=True)
	answer = models.TextField(blank=True)

	def __str__(self):
		return self.question
