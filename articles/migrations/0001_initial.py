# Generated by Django 4.2 on 2023-04-21 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('moderator', '0003_user_dark_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Maqola rukni',
                'verbose_name_plural': '1. Maqola ruknlari',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Jurnal',
                'verbose_name_plural': '2. Jurnallar',
            },
        ),
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='files/post')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=150)),
                ('is_viewed', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('not', "Ko'rilmadi"), ('ok', 'Tasdiqlandi'), ('warning', "Qayta ko'rib chiqilsin"), ('error', 'Qabul qilinmadi')], default='not', max_length=20)),
                ('confirmed', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='moderator.moderator')),
            ],
            options={
                'verbose_name': 'Ariza',
                'verbose_name_plural': '3. Arizalar',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('file', models.FileField(upload_to='files/post')),
                ('approved_date_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/uploader')),
                ('column', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='articles.articlecolumn')),
                ('confirmed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='moderator.moderator')),
                ('journal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.journal')),
            ],
            options={
                'verbose_name': 'Maqola',
                'verbose_name_plural': '4. Maqolalar',
            },
        ),
    ]
