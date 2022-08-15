from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserForm(UserCreationForm):
	'''
	Formulario que utiliza el UserCreationForm incorporado para manejar la creación de usuarios.
	'''
	nombre = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Tu nombre..'}))
	apellidos = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Tus apellidos..'}))
	nombre_de_usuario = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Correo electrónico..'}))
	contraseña1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Contraseña..','class':'contraseña'}))
	contraseña2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Confirmar Contraseña..','class':'contraseña'}))

	#reCAPTCHA token
	token = forms.CharField(
		widget=forms.HiddenInput())

	class Meta:
		model = User
		fields = ('nombre_de_usuario', 'nombre', 'apellidos', 'contraseña1', 'contraseña2', )


class AuthForm(AuthenticationForm):
	'''
	Formulario que utiliza el AuthenticationForm incorporado para gestionar la autentificación de los usuarios.
	'''
	nombre_de_usuario = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Correo electrónico..'}))
	contraseña = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Contraseña..','class':'contraseña'}))

	class Meta:
		model = User
		fields = ('nombre_de_usuario','contraseña', )


class UserProfileForm(forms.ModelForm):
	'''
	Modelo-forma básico para nuestro perfil de usuario que extiende el modelo de usuario de Django.
	'''
	direccion = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	ciudad = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	departamento = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	codigo_postal = forms.CharField(max_length=8, required=True, widget = forms.HiddenInput())
	pais = forms.CharField(max_length=40, required=True, widget = forms.HiddenInput())
	longitud = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())
	latitud = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())

	class Meta:
		model = UserProfile
		fields = ('direccion', 'ciudad', 'departamento', 'codigo_postal',
		 'pais', 'longitud', 'latitud')
         