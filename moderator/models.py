from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.handlers.wsgi import WSGIRequest
from django.conf import settings


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True, upload_to='images/avatar')

    dark_mode = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return '%s %s'%(self.last_name, self.first_name)
        else:
            return self.username
    
    def delete(self, *args, **kwargs):
        if not (self.pk == 1):
            super(User, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not (self.pk == 1) or settings.DEBUG:
            super(User, self).save(*args, **kwargs)

    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = '1. Userlar'



class Moderator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=150, null=True)
    is_created = models.BooleanField(default=False)

    def __str__(self) -> str:
        """ Obyektni str tipida ifodalovchi operator """
        return str(self.user)
    
    def save(self, *args, **kwargs):
        self.user.is_active = True
        self.user.is_staff = True
        self.user.save()
        super(Moderator, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.user.is_staff = False
        self.user.save()
        super(Moderator, self).save(*args, **kwargs)


    def get_moderator_or_None(request: WSGIRequest):
        """ requestda moderator bor yoki yo'qligini aniqlash uchun method """

        if not request.user.is_authenticated:
            return None
        user = request.user
        if not (user.is_active and user.is_staff):
            return None
        try:
            moderator = Moderator.objects.get(user_id=user.pk)
            return moderator
        except:
            return None
    
    class Meta:
        verbose_name = 'Moderator'
        verbose_name_plural = '2. Moderatorlar'