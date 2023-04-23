from django.db import models

from ckeditor.fields import RichTextField

from moderator.models import User, Moderator



class ArticleColumn(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Maqola rukni'
        verbose_name_plural = '1. Maqola ruknlari'



class Journal(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Jurnal'
        verbose_name_plural = '2. Jurnallar'



class Petition(models.Model):
    STATUS = (
        ('not', 'Ko\'rilmadi'),
        ('ok', 'Tasdiqlandi'),
        ('warning', 'Qayta ko\'rib chiqilsin'),
        ('error', 'Qabul qilinmadi')
    )
    # Post uploader
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    # Post
    description = models.TextField()
    file = models.FileField(upload_to='files/post')
    date_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)

    is_viewed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS, default=STATUS[0][0])
    confirmed = models.ForeignKey(Moderator, on_delete=models.SET_DEFAULT, default=1, null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Ariza'
        verbose_name_plural = '3. Arizalar'



class Article(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.SET_NULL, null=True)
    column = models.ForeignKey(ArticleColumn, on_delete=models.SET_DEFAULT, default=1)
    confirmed = models.ForeignKey(Moderator, on_delete=models.SET_NULL, null=True)

    # post
    title = models.CharField(max_length=250)
    file = models.FileField(upload_to='files/post')
    approved_date_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    # uploader
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.title
    
    def upgrade(petition: Petition):
        new_object = Article()
        new_object.title = petition.title
        new_object.file = petition.file
        new_object.confirmed = petition.confirmed
        new_object.description = petition.description
        new_object.first_name = petition.first_name
        new_object.last_name = petition.last_name
        return new_object

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = '4. Maqolalar'






class Post(models.Model):
    author = models.ForeignKey(Moderator, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)

    body = RichTextField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = '5. Postlar'