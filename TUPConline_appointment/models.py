from django.db import models
from django.utils import timezone


class schedule(models.Model):
	fullname = models.CharField(max_length=50, verbose_name='fullname', default="",)
	dept = [
				('reg', 'Register'),
				('OAA', 'Office of Academic Affairs'),
				('OSA', 'Office of Student Affairs'),
				('Campus Director', 'Campus Director'),
				('Uitc', 'University Information Technology Center'),
				('Finance', 'Finance'),
				('Procurement', 'Procurement'),
				('Research and Extension', 'Research and Extension'),
				('PE ', 'Physical Education Faculty'),
				('ie ', 'Industrial Education Faculty'),
				('ms ', 'Math and Science Faculty'),
				('IT ', 'Industrial Technology Faculty'),
				('eng ', 'Engineering Faculty'),
				('liberal', 'Liberal Arts Faculty'),
				('lib ', 'Libary'),
				]
	status = [
 				('Accept', 'Accept'),
				('Deny', 'Deny'),
				('Pending', 'Pending'),
 			]
	category = [
				('Student', 'Student'),
				('Applicant', 'Applicant'),
				('Faculty Member', 'Faculty Member'),
				('Staff','Staff'),
				('Alumnus', 'Alumnus'),
				]
	
	category = models.CharField(max_length =20, choices=category, verbose_name='category', default="---")
	purpose = models.TextField(verbose_name='purpose', default='')
	date = models.DateField(default='')
	created_at = models.DateTimeField(default=timezone.now)
	dept = models.CharField(max_length=50, choices=dept, verbose_name = 'department', default="")
	status = models.TextField(max_length =20, choices=status, verbose_name='status', default="pending", null=True )
	def __str__(self):
		return self.purpose










class Login(models.Model):
	
	username = models.TextField(default="")
	password = models.TextField(default="", max_length=10)

	def __str__(self):
	
		return self.UserName
# Create your models here.