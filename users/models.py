from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    '''
    Extensión del modelo por defecto de Django User Model
    '''
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    direccion = models.CharField(verbose_name='Dirección',max_length=100, null=True, blank=True)
    ciudad = models.CharField(verbose_name='Ciudad/Pueblo',max_length=100, null=True, blank=True)
    departamento = models.CharField(verbose_name='Departamento',max_length=100, null=True, blank=True)
    codigo_postal = models.CharField(verbose_name='Código Postal',max_length=8, null=True, blank=True)
    pais = models.CharField(verbose_name='País',max_length=100, null=True, blank=True)
    longitud = models.CharField(verbose_name='Longitud',max_length=50, null=True, blank=True)
    latitud = models.CharField(verbose_name='Latitud',max_length=50, null=True, blank=True)

    captcha_score = models.FloatField(default=0.0)
    has_profile = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.user}'
