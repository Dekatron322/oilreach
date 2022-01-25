from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput, Select
from django.utils import timezone



class Contact(models.Model):
	name = models.CharField(blank=True, max_length=100)
	email = models.CharField(blank=True, max_length=100)
	phone = models.CharField(blank=True, max_length=100)

	message = models.TextField()
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'message', 'phone']
		widgets = {
			'name'		: TextInput(attrs={'class': 'input','placeholder':'Name & Surname'}),
			'phone'		: TextInput(attrs={'class': 'input','placeholder':'Phone Number'}),
			'email'		: TextInput(attrs={'class': 'input','placeholder':'Email Address'}),
			'message'	: Textarea(attrs={'class': 'input', 'placeholder':'Your Message', 'rows':'5'}),

		}
