# Generated by Django 3.1.1 on 2020-10-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_slug',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(blank=True, to='BlogApp.Views'),
        ),
    ]