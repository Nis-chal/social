# Generated by Django 3.2 on 2021-09-30 10:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import profile_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('portfolio_site', models.URLField(blank=True, validators=[django.core.validators.MaxLengthValidator(200)])),
                ('profile_pic', models.ImageField(blank=True, default='def.jpg', upload_to=profile_app.models.profile_pic_directory)),
                ('bio', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50)])),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('followers', models.ManyToManyField(blank=True, default=[0], related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, default=[0], related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, validators=[django.core.validators.MaxLengthValidator(8)])),
            ],
        ),
    ]
