# Generated by Django 3.1.1 on 2020-10-12 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0003_auto_20201011_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ('-date',)},
        ),
    ]
