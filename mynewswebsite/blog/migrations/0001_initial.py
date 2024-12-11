# Generated by Django 5.1.2 on 2024-11-04 21:20

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('short_description', models.TextField()),
                ('content', models.TextField()),
                ('banner_path', models.ImageField(upload_to='news_bannner')),
                ('status', models.BooleanField(default=False, null=True, verbose_name='staff status')),
                ('meta_keywords', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(default='', unique=True)),
                ('seotitle', models.TextField(default='')),
                ('seo_description', models.TextField(default='')),
                ('seo_script', models.TextField(default='')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
