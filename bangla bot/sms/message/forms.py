from django import forms
from message.models import Contact
from django.contrib.auth.models import User



class MessageForm(forms.Form):
	
	#campaign=forms.CharField(required = False ,max_length=255,label="Campaign Name")
	#user_id=forms.CharField(required = False ,max_length=13,label="User ID")
	user = forms.ModelChoiceField(queryset= User.objects.all(),required = False)
	#contact = forms.ModelChoiceField(queryset= Contact.objects.all(),required = False)
	#contact = forms.ModelChoiceField(widget=forms.Select,queryset=Post) #err
	message = forms.CharField(required = False,widget=forms.Textarea(attrs={'name':'message','rows':9,'cols':26}))
	#ckbox= forms.MultipleChoiceField(widget=forms.CheckboxSeletMultiple,choices=[(i.nane,i.name) for in Post.objects.all()])
	#choices=[('1','Roman'),('2','Rokon')]
	#choices=[(i.title, i.title) for i in Post.objects.all()]
	#contact= forms.MultipleChoiceField(choices=choices,required=False)
	#cfield= forms.ChoiceField(required=False,initial='mystring',choices=choices,widget=forms.RadioSelect())



class GMessageForm(forms.Form):
	
	
	#user_id=forms.CharField(required = False ,max_length=13,label="User ID")
	user = forms.ModelChoiceField(queryset= User.objects.all(),required = False)
	category = forms.ModelChoiceField(queryset= Contact.objects.all(),required = False)
	#contact = forms.ModelChoiceField(widget=forms.Select,queryset=Post) #err
	question=forms.CharField(required = False ,max_length=255,label="Question")
	answer = forms.CharField(required = False,widget=forms.Textarea(attrs={'name':'message','rows':9,'cols':26}))
	#ckbox= forms.MultipleChoiceField(widget=forms.CheckboxSeletMultiple,choices=[(i.nane,i.name) for in Post.objects.all()])
	#choices=[('1','Roman'),('2','Rokon')]
	#choices=[(i.title, i.title) for i in Post.objects.all()]
	#contact= forms.MultipleChoiceField(choices=choices,required=False)
	#cfield= forms.ChoiceField(required=False,initial='mystring',choices=choices,widget=forms.RadioSelect())
		

class ContactForm(forms.Form):
	

	#user_id=forms.CharField(required = False ,max_length=13,label="User ID")
	user = forms.ModelChoiceField(queryset= User.objects.all(),required = False)
	Page_name=forms.CharField(required = False ,max_length=13,label="Page Name")
	Page_access_token =forms.CharField(required = False ,max_length=13,label="Page_access_token")
	#contact = forms.ModelChoiceField(widget=forms.Select,queryset=Post) #err
	webhook_url = forms.CharField(required = False,widget=forms.Textarea(attrs={'name':'message','rows':9,'cols':26}))
	#ckbox= forms.MultipleChoiceField(widget=forms.CheckboxSeletMultiple,choices=[(i.nane,i.name) for in Post.objects.all()])
	#choices=[('1','Roman'),('2','Rokon')]
	#choices=[(i.title, i.title) for i in Post.objects.all()]
	#contact= forms.MultipleChoiceField(choices=choices,required=False)
	#cfield= forms.ChoiceField(required=False,initial='mystring',choices=choices,widget=forms.RadioSelect())
	


class GContactForm(forms.Form):
	

	#user_id=forms.CharField(required = False ,max_length=13,label="User ID")
	user = forms.ModelChoiceField(queryset= User.objects.all(),required = False)
	group_name=forms.CharField(required = False ,max_length=13,label="Group Name")
	contacts = forms.ModelMultipleChoiceField(queryset= Contact.objects.all(),required = False)
	#contact = forms.ModelChoiceField(widget=forms.Select,queryset=Post) #err
	info = forms.CharField(required = False,widget=forms.Textarea(attrs={'name':'message','rows':9,'cols':26}))
	#ckbox= forms.MultipleChoiceField(widget=forms.CheckboxSeletMultiple,choices=[(i.nane,i.name) for in Post.objects.all()])
	#choices=[('1','Roman'),('2','Rokon')]
	#choices=[(i.title, i.title) for i in Post.objects.all()]
	#contact= forms.MultipleChoiceField(choices=choices,required=False)
	#cfield= forms.ChoiceField(required=False,initial='mystring',choices=choices,widget=forms.RadioSelect())
	


'''


class SingInForm(forms.Form):
	user_name=forms.CharField(label='Your User Name',max_length=25)
	email=forms.EmailField(label='Enter Email ',max_length=25)
	password=forms.CharField(label='Your Password',max_length=25)


class SingUpForm(forms.Form):
	user_name=forms.CharField(label='Your User Name',max_length=25)
	email=forms.EmailField(label='Enter Email ',max_length=25)
	password=forms.CharField(label='Your Password',max_length=25)



  '''