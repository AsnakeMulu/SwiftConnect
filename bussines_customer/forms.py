from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.safestring import mark_safe


class NewUserForm(UserCreationForm):
	
	email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
	first_name = forms.CharField(max_length=20, label= 'First Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'text-black'}))
	last_name = forms.CharField(max_length=20, label= 'Last Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'text-black'}))
	#phone_number = forms.CharField(max_length=20, label= 'Phone Number', required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'text-black'}))
	password1 = forms.CharField(max_length=100, label= 'Password', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'text-black'}))
	password2 = forms.CharField(max_length=100, label= 'Confirm Password', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'text-black'}))
	is_agreed= forms.BooleanField(label= mark_safe('I agree with the <a href="/terms" style="color: blue;">terms and conditions</a>'), required=True, widget=forms.CheckboxInput(attrs={'placeholder': 'Invited By', 'class': 'text-black'}))
	
	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email", "password1", "password2")
		widgets = {
			'username': forms.TextInput(attrs={'placeholder': 'UserName', 'class': 'text-black'}),
			'password1': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'text-black'}),
			#'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].help_text=''
		self.fields['password1'].help_text=''
		self.fields['password2'].help_text=''


	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']
		#user.password = self.cleaned_data['password1']
		if commit:
			user.save()
		return user
	
class RequestForm(forms.Form):
	sender_BIC = forms.CharField(label='Sender BIC', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Write here Sender BIC', 'class': 'text-black'}))
	sender_name = forms.CharField(label='Sender Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Write here Sender Name', 'class': 'text-black'}))
	receiver_BIC= forms.CharField(label='Receiver BIC', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Write here Receiver BIC', 'class': 'text-black'}))
	receiver_name = forms.CharField(label='Receiver Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Write here Receiver Name', 'class': 'text-black'}))
	request_description = forms.CharField(label='Request Description', max_length=1000, widget=forms.Textarea(attrs={'placeholder': 'Describe your order as much details as possible', 'class': 'text-black'}))
