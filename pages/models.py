from django.db import models

from ckeditor.fields import RichTextField





class Icon(models.Model):
    image = models.ImageField(upload_to='images/icon')

    def __str__(self) -> str:
        return self.image.name
    
    def object():
        return Icon.objects.get(pk=1)
    
    def save(self, *args, **kwargs):
        if self.pk == 1:
            super(Icon, self).save(*args, **kwargs)

    def as_dict():
        return {
            'image': Icon.object().image.url
        }

    def delete(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = 'Ikonka'
        verbose_name_plural = '1. Ikonka'




class IjtimoiyTarmoqlar(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='images/tarmoq/icon')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Ijtimoiy tarmoq'
        verbose_name_plural = '2. Ijtimoiy tarmoqlar'


class Eslatma(models.Model):
    name = models.CharField(max_length=100)
    body = RichTextField()

    def __str__(self) -> str:
        return self.name
    
    def object():
        return Eslatma.objects.get(pk=1)

    def save(self, *args, **kwargs):
        if self.pk == 1:
            super(Eslatma, self).save(*args, **kwargs)

    def as_dict():
        object = Eslatma.object()
        return {
            'name': object.name,
            'body': object.body
        }

    def delete(self, *args, **kwargs):
        pass
    
    class Meta:
        verbose_name = 'Eslatma'
        verbose_name_plural = 'Eslatma'



class MaqolaJoylash(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/info')
    body = RichTextField()

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if self.pk == 1:
            super(MaqolaJoylash, self).save(*args, **kwargs)
    
    def as_dict():
        object = MaqolaJoylash.object()
        return {
            'name': object.name,
            'short_name': object.short_name,
            'image': object.image.url,
            'body': object.body,
        }

    def delete(self, *args, **kwargs):
        pass

    def object():
        return MaqolaJoylash.objects.get(pk=1)
    
    class Meta:
        verbose_name = 'Maqola joylash'
        verbose_name_plural = 'Maqola joylash'


class Narxlar(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/narxlar')
    body = RichTextField()

    def __str__(self) -> str:
        return self.name
    
    def delete(self, *args, **kwargs):
        pass
    
    def save(self, *args, **kwargs):
        if self.pk == 1:
            super(Narxlar, self).save(*args, **kwargs)

    def as_dict():
        object = Narxlar.object()
        return {
            'name': object.name,
            'short_name': object.short_name,
            'image': object.image.url,
            'body': object.body
        }

    def object():
        return Narxlar.objects.get(pk=1)
    
    class Meta:
        verbose_name = 'Narxlar'
        verbose_name_plural = 'Narxlar'


class Manzili(models.Model):
    manzil = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.manzil
    
    def delete(self, *args, **kwargs):
        pass

    def save(self, *args, **kwargs):
        if self.pk == 1:
            super(Manzili, self).save(*args, **kwargs)

    def as_dict():
        return {
            'manzil': Manzili.object().manzil
        }

    def object():
        return Manzili.objects.get(pk=1)
    
    class Meta:
        verbose_name = 'Manzil'
        verbose_name_plural = 'Manzil'