# Generated by Django 4.2.6 on 2023-11-06 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_profesor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='comision',
            new_name='camada',
        ),
    ]
