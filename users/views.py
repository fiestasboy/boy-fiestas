from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

from boyFiestas.mixins import(
	AjaxFormMixin, 
	reCAPTCHAValidation,
	FormErrors,
	RedirectParams,
	)

from .forms import (
	UserForm,
	UserProfileForm,
	AuthForm,
	)


result = "Error"
message = "Ha habido un error, por favor inténtelo de nuevo."


class AccountView(TemplateView):
	'''
	FormView genérico con nuestro mixin para mostrar la página de la cuenta de usuario.
	'''
	template_name = "users/account.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)



def profile_view(request):
	'''
	Vista de la función para permitir a los usuarios actualizar su perfil.
	'''
	user = request.user
	up = user.userprofile

	form = UserProfileForm(instance = up) 

	if request.headers.get('x-requested-with') == 'XMLHttpRequest':
		form = UserProfileForm(data = request.POST, instance = up)
		if form.is_valid():
			obj = form.save()
			obj.has_profile = True
			obj.save()
			result = "Success"
			message = "Su perfil ha sido actualizado"
		else:
			message = FormErrors(form)
		data = {'result': result, 'message': message}
		return JsonResponse(data)

	else:

		context = {'form': form}
		context['google_api_key'] = settings.GOOGLE_API_KEY
		context['base_country'] = settings.BASE_COUNTRY

		return render(request, 'users/profile.html', context)



class SignUpView(AjaxFormMixin, FormView):
	'''
	FormView genérico con nuestro mixin para el registro de usuarios con seguridad reCAPTURE.
	'''

	template_name = "users/sign_up.html"
	form_class = UserForm
	success_url = "/"

	#reCAPTURE key required in context
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["recaptcha_site_key"] = settings.RECAPTCHA_PUBLIC_KEY
		return context

	#over write the mixin logic to get, check and save reCAPTURE score
	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)	
		if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
			token = form.cleaned_data.get('token')
			captcha = reCAPTCHAValidation(token)
			if captcha["success"]:
				obj = form.save()
				obj.correo = obj.username
				obj.save()
				up = obj.userprofile
				up.captcha_score = float(captcha["score"])
				up.save()
				
				login(self.request, obj, backend='django.contrib.auth.backends.ModelBackend')

				#change result & message on success
				result = "Success"
				message = "Gracias por registrarte"

				
			data = {'result': result, 'message': message}
			return JsonResponse(data)

		return response




class SignInView(AjaxFormMixin, FormView):
	'''
	FormView genérico con nuestro mixin para el registro de usuarios.
	'''

	template_name = "users/sign_in.html"
	form_class = AuthForm
	success_url = "/"

	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)	
		if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			#Intento de autentificar al usuario.
			user = authenticate(self.request, username=username, password=password)
			if user is not None:
				login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
				result = "Success"
				message = 'Ya has iniciado sesión'
			else:
				message = FormErrors(form)
			data = {'result': result, 'message': message}
			return JsonResponse(data)
		return response




def sign_out(request):
	'''
	Vista básica para el cierre de sesión del usuario.
	'''
	logout(request)
	return redirect(reverse('users:sign-in'))

