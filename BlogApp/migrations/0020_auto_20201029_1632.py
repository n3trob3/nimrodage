# Generated by Django 3.1.1 on 2020-10-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0019_auto_20201017_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='EmailMarketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('receivers', models.ManyToManyField(related_name='Receivers', to='BlogApp.Newsletter')),
                ('rejects', models.ManyToManyField(to='BlogApp.Newsletter')),
                ('sents', models.ManyToManyField(related_name='Sents', to='BlogApp.Newsletter')),
            ],
        ),
    ]
